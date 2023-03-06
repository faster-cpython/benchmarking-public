
# Results vs. 3.10.4

- fork: gvanrossum
- ref: tagged_ptrs
- machine: linux-x86_64
- commit hash: 3b7866f
- commit date: 2023-03-05
- overall geometric mean: 1.26x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230305-linux-x86_64-gvanrossum-tagged_ptrs-3.12.0a5+-3b7866f |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 335 ms                                                 | 255 ms: 1.31x faster                                              |
| chameleon      | 9.17 ms                                                | 6.64 ms: 1.38x faster                                             |
| docutils       | 3.18 sec                                               | 2.59 sec: 1.23x faster                                            |
| html5lib       | 85.9 ms                                                | 63.2 ms: 1.36x faster                                             |
| tornado_http   | 128 ms                                                 | 96.0 ms: 1.34x faster                                             |
| Geometric mean | (ref)                                                  | 1.32x faster                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230305-linux-x86_64-gvanrossum-tagged_ptrs-3.12.0a5+-3b7866f |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| float          | 109 ms                                                 | 76.0 ms: 1.43x faster                                             |
| nbody          | 144 ms                                                 | 101 ms: 1.43x faster                                              |
| pidigits       | 190 ms                                                 | 193 ms: 1.01x slower                                              |
| Geometric mean | (ref)                                                  | 1.26x faster                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230305-linux-x86_64-gvanrossum-tagged_ptrs-3.12.0a5+-3b7866f |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 138 ms: 1.29x faster                                              |
| regex_v8       | 25.0 ms                                                | 22.5 ms: 1.12x faster                                             |
| regex_dna      | 214 ms                                                 | 207 ms: 1.03x faster                                              |
| regex_effbot   | 3.19 ms                                                | 3.36 ms: 1.05x slower                                             |
| Geometric mean | (ref)                                                  | 1.09x faster                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230305-linux-x86_64-gvanrossum-tagged_ptrs-3.12.0a5+-3b7866f |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| pickle_pure_python   | 452 us                                                 | 297 us: 1.53x faster                                              |
| unpickle_pure_python | 302 us                                                 | 208 us: 1.45x faster                                              |
| json_dumps           | 13.4 ms                                                | 9.58 ms: 1.40x faster                                             |
| xml_etree_process    | 74.5 ms                                                | 57.4 ms: 1.30x faster                                             |
| json_loads           | 28.7 us                                                | 23.7 us: 1.21x faster                                             |
| xml_etree_generate   | 93.8 ms                                                | 83.1 ms: 1.13x faster                                             |
| pickle_list          | 4.72 us                                                | 4.24 us: 1.11x faster                                             |
| xml_etree_iterparse  | 111 ms                                                 | 101 ms: 1.10x faster                                              |
| xml_etree_parse      | 163 ms                                                 | 149 ms: 1.10x faster                                              |
| unpickle             | 14.2 us                                                | 13.7 us: 1.04x faster                                             |
| unpickle_list        | 4.92 us                                                | 5.11 us: 1.04x slower                                             |
| pickle_dict          | 27.6 us                                                | 31.3 us: 1.14x slower                                             |
| Geometric mean       | (ref)                                                  | 1.15x faster                                                      |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230305-linux-x86_64-gvanrossum-tagged_ptrs-3.12.0a5+-3b7866f |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                | 9.02 ms: 1.56x faster                                             |
| python_startup_no_site | 5.78 ms                                                | 6.54 ms: 1.13x slower                                             |
| Geometric mean         | (ref)                                                  | 1.17x faster                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230305-linux-x86_64-gvanrossum-tagged_ptrs-3.12.0a5+-3b7866f |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| mako            | 14.7 ms                                                | 10.5 ms: 1.40x faster                                             |
| genshi_text     | 30.6 ms                                                | 22.0 ms: 1.39x faster                                             |
| django_template | 46.3 ms                                                | 34.3 ms: 1.35x faster                                             |
| genshi_xml      | 63.7 ms                                                | 49.7 ms: 1.28x faster                                             |
| Geometric mean  | (ref)                                                  | 1.36x faster                                                      |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230305-linux-x86_64-gvanrossum-tagged_ptrs-3.12.0a5+-3b7866f |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| generators              | 76.4 ms                                                | 31.3 ms: 2.44x faster                                             |
| deltablue               | 7.28 ms                                                | 3.34 ms: 2.18x faster                                             |
| asyncio_tcp             | 914 ms                                                 | 505 ms: 1.81x faster                                              |
| logging_silent          | 176 ns                                                 | 98.7 ns: 1.79x faster                                             |
| scimark_sor             | 197 ms                                                 | 115 ms: 1.71x faster                                              |
| richards                | 75.2 ms                                                | 44.3 ms: 1.70x faster                                             |
| go                      | 226 ms                                                 | 140 ms: 1.61x faster                                              |
| pyflate                 | 676 ms                                                 | 420 ms: 1.61x faster                                              |
| python_startup          | 14.1 ms                                                | 9.02 ms: 1.56x faster                                             |
| raytrace                | 467 ms                                                 | 299 ms: 1.56x faster                                              |
| crypto_pyaes            | 117 ms                                                 | 75.9 ms: 1.54x faster                                             |
| scimark_monte_carlo     | 109 ms                                                 | 70.9 ms: 1.53x faster                                             |
| pickle_pure_python      | 452 us                                                 | 297 us: 1.53x faster                                              |
| chaos                   | 106 ms                                                 | 70.7 ms: 1.49x faster                                             |
| spectral_norm           | 150 ms                                                 | 102 ms: 1.46x faster                                              |
| unpickle_pure_python    | 302 us                                                 | 208 us: 1.45x faster                                              |
| hexiom                  | 9.43 ms                                                | 6.49 ms: 1.45x faster                                             |
| float                   | 109 ms                                                 | 76.0 ms: 1.43x faster                                             |
| nbody                   | 144 ms                                                 | 101 ms: 1.43x faster                                              |
| json_dumps              | 13.4 ms                                                | 9.58 ms: 1.40x faster                                             |
| deepcopy_memo           | 51.7 us                                                | 36.8 us: 1.40x faster                                             |
| scimark_lu              | 161 ms                                                 | 115 ms: 1.40x faster                                              |
| mako                    | 14.7 ms                                                | 10.5 ms: 1.40x faster                                             |
| genshi_text             | 30.6 ms                                                | 22.0 ms: 1.39x faster                                             |
| sqlglot_parse           | 2.04 ms                                                | 1.48 ms: 1.38x faster                                             |
| chameleon               | 9.17 ms                                                | 6.64 ms: 1.38x faster                                             |
| logging_format          | 8.85 us                                                | 6.46 us: 1.37x faster                                             |
| logging_simple          | 8.10 us                                                | 5.92 us: 1.37x faster                                             |
| pprint_pformat          | 1.98 sec                                               | 1.45 sec: 1.37x faster                                            |
| sqlglot_transpile       | 2.43 ms                                                | 1.78 ms: 1.36x faster                                             |
| html5lib                | 85.9 ms                                                | 63.2 ms: 1.36x faster                                             |
| async_tree_io           | 1.78 sec                                               | 1.31 sec: 1.36x faster                                            |
| django_template         | 46.3 ms                                                | 34.3 ms: 1.35x faster                                             |
| pycparser               | 1.53 sec                                               | 1.14 sec: 1.35x faster                                            |
| async_tree_none         | 711 ms                                                 | 529 ms: 1.34x faster                                              |
| pprint_safe_repr        | 953 ms                                                 | 710 ms: 1.34x faster                                              |
| tornado_http            | 128 ms                                                 | 96.0 ms: 1.34x faster                                             |
| unpack_sequence         | 59.4 ns                                                | 44.8 ns: 1.33x faster                                             |
| thrift                  | 1.03 ms                                                | 783 us: 1.32x faster                                              |
| coroutines              | 31.6 ms                                                | 24.0 ms: 1.32x faster                                             |
| 2to3                    | 335 ms                                                 | 255 ms: 1.31x faster                                              |
| aiohttp                 | 1.34 ms                                                | 1.02 ms: 1.31x faster                                             |
| gunicorn                | 1.43 ms                                                | 1.10 ms: 1.30x faster                                             |
| xml_etree_process       | 74.5 ms                                                | 57.4 ms: 1.30x faster                                             |
| regex_compile           | 177 ms                                                 | 138 ms: 1.29x faster                                              |
| genshi_xml              | 63.7 ms                                                | 49.7 ms: 1.28x faster                                             |
| async_tree_memoization  | 855 ms                                                 | 670 ms: 1.28x faster                                              |
| fannkuch                | 488 ms                                                 | 385 ms: 1.27x faster                                              |
| async_tree_cpu_io_mixed | 949 ms                                                 | 750 ms: 1.27x faster                                              |
| mypy2                   | 430 ms                                                 | 340 ms: 1.27x faster                                              |
| deepcopy                | 438 us                                                 | 346 us: 1.26x faster                                              |
| scimark_fft             | 421 ms                                                 | 337 ms: 1.25x faster                                              |
| sqlglot_normalize       | 134 ms                                                 | 108 ms: 1.25x faster                                              |
| sqlglot_optimize        | 65.2 ms                                                | 52.6 ms: 1.24x faster                                             |
| docutils                | 3.18 sec                                               | 2.59 sec: 1.23x faster                                            |
| deepcopy_reduce         | 3.79 us                                                | 3.12 us: 1.21x faster                                             |
| json_loads              | 28.7 us                                                | 23.7 us: 1.21x faster                                             |
| sqlalchemy_declarative  | 165 ms                                                 | 140 ms: 1.18x faster                                              |
| dulwich_log             | 75.8 ms                                                | 64.3 ms: 1.18x faster                                             |
| sqlalchemy_imperative   | 21.5 ms                                                | 18.3 ms: 1.17x faster                                             |
| json                    | 5.35 ms                                                | 4.56 ms: 1.17x faster                                             |
| bench_thread_pool       | 946 us                                                 | 808 us: 1.17x faster                                              |
| nqueens                 | 100 ms                                                 | 86.7 ms: 1.15x faster                                             |
| sympy_integrate         | 24.0 ms                                                | 20.9 ms: 1.15x faster                                             |
| sympy_expand            | 534 ms                                                 | 467 ms: 1.14x faster                                              |
| xml_etree_generate      | 93.8 ms                                                | 83.1 ms: 1.13x faster                                             |
| create_gc_cycles        | 1.65 ms                                                | 1.47 ms: 1.13x faster                                             |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.86 ms: 1.12x faster                                             |
| sympy_str               | 325 ms                                                 | 291 ms: 1.12x faster                                              |
| pathlib                 | 20.0 ms                                                | 17.9 ms: 1.12x faster                                             |
| regex_v8                | 25.0 ms                                                | 22.5 ms: 1.12x faster                                             |
| djangocms               | 36.9 us                                                | 33.1 us: 1.11x faster                                             |
| pickle_list             | 4.72 us                                                | 4.24 us: 1.11x faster                                             |
| sqlite_synth            | 2.92 us                                                | 2.63 us: 1.11x faster                                             |
| xml_etree_iterparse     | 111 ms                                                 | 101 ms: 1.10x faster                                              |
| xml_etree_parse         | 163 ms                                                 | 149 ms: 1.10x faster                                              |
| meteor_contest          | 114 ms                                                 | 105 ms: 1.09x faster                                              |
| sympy_sum               | 183 ms                                                 | 169 ms: 1.08x faster                                              |
| unpickle                | 14.2 us                                                | 13.7 us: 1.04x faster                                             |
| mdp                     | 2.74 sec                                               | 2.66 sec: 1.03x faster                                            |
| regex_dna               | 214 ms                                                 | 207 ms: 1.03x faster                                              |
| telco                   | 6.73 ms                                                | 6.59 ms: 1.02x faster                                             |
| async_generators        | 426 ms                                                 | 423 ms: 1.01x faster                                              |
| pidigits                | 190 ms                                                 | 193 ms: 1.01x slower                                              |
| unpickle_list           | 4.92 us                                                | 5.11 us: 1.04x slower                                             |
| regex_effbot            | 3.19 ms                                                | 3.36 ms: 1.05x slower                                             |
| python_startup_no_site  | 5.78 ms                                                | 6.54 ms: 1.13x slower                                             |
| pickle_dict             | 27.6 us                                                | 31.3 us: 1.14x slower                                             |
| gc_traversal            | 3.53 ms                                                | 4.07 ms: 1.15x slower                                             |
| dask                    | 436 ms                                                 | 517 ms: 1.18x slower                                              |
| coverage                | 74.7 ms                                                | 97.0 ms: 1.30x slower                                             |
| Geometric mean          | (ref)                                                  | 1.26x faster                                                      |

Benchmark hidden because not significant (2): bench_mp_pool, pickle
Ignored benchmarks (2) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, pylint
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230305-3.12.0a5+-3b7866f/bm-20230305-linux-x86_64-gvanrossum-tagged_ptrs-3.12.0a5+-3b7866f.json: comprehensions
