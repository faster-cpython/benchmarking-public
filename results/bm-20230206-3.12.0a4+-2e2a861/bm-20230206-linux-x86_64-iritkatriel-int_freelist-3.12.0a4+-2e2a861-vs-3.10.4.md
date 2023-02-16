
# Results vs. 3.10.4

- fork: iritkatriel
- ref: int_freelist
- machine: linux-x86_64
- commit hash: 2e2a861
- commit date: 2023-02-06
- overall geometric mean: 1.30x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230206-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-2e2a861 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 335 ms                                                 | 252 ms: 1.33x faster                                                |
| chameleon      | 9.17 ms                                                | 6.35 ms: 1.44x faster                                               |
| docutils       | 3.18 sec                                               | 2.49 sec: 1.27x faster                                              |
| html5lib       | 85.9 ms                                                | 60.3 ms: 1.42x faster                                               |
| tornado_http   | 128 ms                                                 | 93.9 ms: 1.36x faster                                               |
| Geometric mean | (ref)                                                  | 1.37x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230206-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-2e2a861 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| nbody          | 144 ms                                                 | 95.9 ms: 1.50x faster                                               |
| float          | 109 ms                                                 | 73.2 ms: 1.49x faster                                               |
| pidigits       | 190 ms                                                 | 203 ms: 1.07x slower                                                |
| Geometric mean | (ref)                                                  | 1.28x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230206-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-2e2a861 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 128 ms: 1.39x faster                                                |
| regex_v8       | 25.0 ms                                                | 22.4 ms: 1.12x faster                                               |
| regex_dna      | 214 ms                                                 | 207 ms: 1.03x faster                                                |
| regex_effbot   | 3.19 ms                                                | 3.51 ms: 1.10x slower                                               |
| Geometric mean | (ref)                                                  | 1.10x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230206-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-2e2a861 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| pickle_pure_python   | 452 us                                                 | 285 us: 1.59x faster                                                |
| unpickle_pure_python | 302 us                                                 | 200 us: 1.51x faster                                                |
| json_dumps           | 13.4 ms                                                | 9.34 ms: 1.44x faster                                               |
| xml_etree_process    | 74.5 ms                                                | 53.4 ms: 1.40x faster                                               |
| json_loads           | 28.7 us                                                | 23.5 us: 1.22x faster                                               |
| xml_etree_generate   | 93.8 ms                                                | 77.5 ms: 1.21x faster                                               |
| pickle_list          | 4.72 us                                                | 4.22 us: 1.12x faster                                               |
| xml_etree_parse      | 163 ms                                                 | 147 ms: 1.11x faster                                                |
| xml_etree_iterparse  | 111 ms                                                 | 103 ms: 1.08x faster                                                |
| unpickle             | 14.2 us                                                | 13.1 us: 1.08x faster                                               |
| unpickle_list        | 4.92 us                                                | 4.98 us: 1.01x slower                                               |
| pickle_dict          | 27.6 us                                                | 31.5 us: 1.14x slower                                               |
| Geometric mean       | (ref)                                                  | 1.18x faster                                                        |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230206-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-2e2a861 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                | 8.96 ms: 1.57x faster                                               |
| python_startup_no_site | 5.78 ms                                                | 6.49 ms: 1.12x slower                                               |
| Geometric mean         | (ref)                                                  | 1.18x faster                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230206-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-2e2a861 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako            | 14.7 ms                                                | 9.46 ms: 1.55x faster                                               |
| genshi_text     | 30.6 ms                                                | 20.7 ms: 1.48x faster                                               |
| django_template | 46.3 ms                                                | 32.5 ms: 1.43x faster                                               |
| genshi_xml      | 63.7 ms                                                | 46.5 ms: 1.37x faster                                               |
| Geometric mean  | (ref)                                                  | 1.45x faster                                                        |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230206-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-2e2a861 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| deltablue               | 7.28 ms                                                | 3.21 ms: 2.27x faster                                               |
| logging_silent          | 176 ns                                                 | 92.2 ns: 1.91x faster                                               |
| scimark_sor             | 197 ms                                                 | 106 ms: 1.85x faster                                                |
| asyncio_tcp             | 914 ms                                                 | 494 ms: 1.85x faster                                                |
| richards                | 75.2 ms                                                | 42.6 ms: 1.77x faster                                               |
| pyflate                 | 676 ms                                                 | 395 ms: 1.71x faster                                                |
| go                      | 226 ms                                                 | 135 ms: 1.67x faster                                                |
| raytrace                | 467 ms                                                 | 284 ms: 1.65x faster                                                |
| scimark_monte_carlo     | 109 ms                                                 | 66.6 ms: 1.63x faster                                               |
| chaos                   | 106 ms                                                 | 64.9 ms: 1.63x faster                                               |
| pickle_pure_python      | 452 us                                                 | 285 us: 1.59x faster                                                |
| python_startup          | 14.1 ms                                                | 8.96 ms: 1.57x faster                                               |
| spectral_norm           | 150 ms                                                 | 95.5 ms: 1.57x faster                                               |
| hexiom                  | 9.43 ms                                                | 6.02 ms: 1.57x faster                                               |
| mako                    | 14.7 ms                                                | 9.46 ms: 1.55x faster                                               |
| crypto_pyaes            | 117 ms                                                 | 75.7 ms: 1.54x faster                                               |
| scimark_lu              | 161 ms                                                 | 106 ms: 1.52x faster                                                |
| unpickle_pure_python    | 302 us                                                 | 200 us: 1.51x faster                                                |
| nbody                   | 144 ms                                                 | 95.9 ms: 1.50x faster                                               |
| deepcopy_memo           | 51.7 us                                                | 34.7 us: 1.49x faster                                               |
| float                   | 109 ms                                                 | 73.2 ms: 1.49x faster                                               |
| genshi_text             | 30.6 ms                                                | 20.7 ms: 1.48x faster                                               |
| sqlglot_parse           | 2.04 ms                                                | 1.40 ms: 1.46x faster                                               |
| pprint_pformat          | 1.98 sec                                               | 1.36 sec: 1.45x faster                                              |
| chameleon               | 9.17 ms                                                | 6.35 ms: 1.44x faster                                               |
| json_dumps              | 13.4 ms                                                | 9.34 ms: 1.44x faster                                               |
| pprint_safe_repr        | 953 ms                                                 | 666 ms: 1.43x faster                                                |
| django_template         | 46.3 ms                                                | 32.5 ms: 1.43x faster                                               |
| sqlglot_transpile       | 2.43 ms                                                | 1.70 ms: 1.43x faster                                               |
| logging_simple          | 8.10 us                                                | 5.69 us: 1.42x faster                                               |
| html5lib                | 85.9 ms                                                | 60.3 ms: 1.42x faster                                               |
| logging_format          | 8.85 us                                                | 6.32 us: 1.40x faster                                               |
| thrift                  | 1.03 ms                                                | 740 us: 1.40x faster                                                |
| scimark_fft             | 421 ms                                                 | 302 ms: 1.40x faster                                                |
| xml_etree_process       | 74.5 ms                                                | 53.4 ms: 1.40x faster                                               |
| regex_compile           | 177 ms                                                 | 128 ms: 1.39x faster                                                |
| unpack_sequence         | 59.4 ns                                                | 42.8 ns: 1.39x faster                                               |
| scimark_sparse_mat_mult | 5.45 ms                                                | 3.96 ms: 1.38x faster                                               |
| async_tree_memoization  | 855 ms                                                 | 624 ms: 1.37x faster                                                |
| genshi_xml              | 63.7 ms                                                | 46.5 ms: 1.37x faster                                               |
| tornado_http            | 128 ms                                                 | 93.9 ms: 1.36x faster                                               |
| async_tree_none         | 711 ms                                                 | 524 ms: 1.36x faster                                                |
| async_tree_io           | 1.78 sec                                               | 1.32 sec: 1.35x faster                                              |
| aiohttp                 | 1.34 ms                                                | 994 us: 1.35x faster                                                |
| fannkuch                | 488 ms                                                 | 363 ms: 1.34x faster                                                |
| pycparser               | 1.53 sec                                               | 1.14 sec: 1.34x faster                                              |
| gunicorn                | 1.43 ms                                                | 1.07 ms: 1.34x faster                                               |
| 2to3                    | 335 ms                                                 | 252 ms: 1.33x faster                                                |
| deepcopy                | 438 us                                                 | 334 us: 1.31x faster                                                |
| coroutines              | 31.6 ms                                                | 24.5 ms: 1.29x faster                                               |
| sqlglot_normalize       | 134 ms                                                 | 105 ms: 1.28x faster                                                |
| nqueens                 | 100 ms                                                 | 78.1 ms: 1.28x faster                                               |
| sqlglot_optimize        | 65.2 ms                                                | 50.9 ms: 1.28x faster                                               |
| deepcopy_reduce         | 3.79 us                                                | 2.97 us: 1.27x faster                                               |
| docutils                | 3.18 sec                                               | 2.49 sec: 1.27x faster                                              |
| async_tree_cpu_io_mixed | 949 ms                                                 | 757 ms: 1.25x faster                                                |
| sympy_integrate         | 24.0 ms                                                | 19.7 ms: 1.22x faster                                               |
| json_loads              | 28.7 us                                                | 23.5 us: 1.22x faster                                               |
| dulwich_log             | 75.8 ms                                                | 62.4 ms: 1.22x faster                                               |
| bench_thread_pool       | 946 us                                                 | 779 us: 1.21x faster                                                |
| async_generators        | 426 ms                                                 | 352 ms: 1.21x faster                                                |
| xml_etree_generate      | 93.8 ms                                                | 77.5 ms: 1.21x faster                                               |
| sympy_str               | 325 ms                                                 | 270 ms: 1.20x faster                                                |
| json                    | 5.35 ms                                                | 4.50 ms: 1.19x faster                                               |
| sympy_sum               | 183 ms                                                 | 156 ms: 1.17x faster                                                |
| sympy_expand            | 534 ms                                                 | 456 ms: 1.17x faster                                                |
| djangocms               | 36.9 us                                                | 31.7 us: 1.16x faster                                               |
| pathlib                 | 20.0 ms                                                | 17.5 ms: 1.14x faster                                               |
| create_gc_cycles        | 1.65 ms                                                | 1.47 ms: 1.13x faster                                               |
| sqlite_synth            | 2.92 us                                                | 2.61 us: 1.12x faster                                               |
| pickle_list             | 4.72 us                                                | 4.22 us: 1.12x faster                                               |
| regex_v8                | 25.0 ms                                                | 22.4 ms: 1.12x faster                                               |
| xml_etree_parse         | 163 ms                                                 | 147 ms: 1.11x faster                                                |
| telco                   | 6.73 ms                                                | 6.17 ms: 1.09x faster                                               |
| meteor_contest          | 114 ms                                                 | 105 ms: 1.09x faster                                                |
| xml_etree_iterparse     | 111 ms                                                 | 103 ms: 1.08x faster                                                |
| unpickle                | 14.2 us                                                | 13.1 us: 1.08x faster                                               |
| mdp                     | 2.74 sec                                               | 2.65 sec: 1.04x faster                                              |
| regex_dna               | 214 ms                                                 | 207 ms: 1.03x faster                                                |
| unpickle_list           | 4.92 us                                                | 4.98 us: 1.01x slower                                               |
| generators              | 76.4 ms                                                | 78.7 ms: 1.03x slower                                               |
| pidigits                | 190 ms                                                 | 203 ms: 1.07x slower                                                |
| gc_traversal            | 3.53 ms                                                | 3.87 ms: 1.10x slower                                               |
| regex_effbot            | 3.19 ms                                                | 3.51 ms: 1.10x slower                                               |
| python_startup_no_site  | 5.78 ms                                                | 6.49 ms: 1.12x slower                                               |
| dask                    | 436 ms                                                 | 493 ms: 1.13x slower                                                |
| pickle_dict             | 27.6 us                                                | 31.5 us: 1.14x slower                                               |
| coverage                | 74.7 ms                                                | 96.8 ms: 1.29x slower                                               |
| Geometric mean          | (ref)                                                  | 1.30x faster                                                        |

Benchmark hidden because not significant (2): pickle, bench_mp_pool
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230206-3.12.0a4+-2e2a861/bm-20230206-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-2e2a861.json: mypy
