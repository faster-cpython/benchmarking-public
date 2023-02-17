
# Results vs. 3.10.4

- fork: iritkatriel
- ref: single_arg_exit
- machine: linux-x86_64
- commit hash: b560583
- commit date: 2023-02-17
- overall geometric mean: 1.31x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230217-linux-x86_64-iritkatriel-single_arg_exit-3.12.0a5+-b560583 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 335 ms                                                 | 246 ms: 1.36x faster                                                   |
| chameleon      | 9.17 ms                                                | 6.29 ms: 1.46x faster                                                  |
| docutils       | 3.18 sec                                               | 2.54 sec: 1.25x faster                                                 |
| html5lib       | 85.9 ms                                                | 61.7 ms: 1.39x faster                                                  |
| tornado_http   | 128 ms                                                 | 95.2 ms: 1.35x faster                                                  |
| Geometric mean | (ref)                                                  | 1.36x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230217-linux-x86_64-iritkatriel-single_arg_exit-3.12.0a5+-b560583 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 144 ms                                                 | 93.1 ms: 1.55x faster                                                  |
| float          | 109 ms                                                 | 72.5 ms: 1.50x faster                                                  |
| pidigits       | 190 ms                                                 | 189 ms: 1.00x faster                                                   |
| Geometric mean | (ref)                                                  | 1.33x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230217-linux-x86_64-iritkatriel-single_arg_exit-3.12.0a5+-b560583 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 129 ms: 1.37x faster                                                   |
| regex_v8       | 25.0 ms                                                | 21.3 ms: 1.17x faster                                                  |
| regex_dna      | 214 ms                                                 | 212 ms: 1.01x faster                                                   |
| regex_effbot   | 3.19 ms                                                | 3.28 ms: 1.03x slower                                                  |
| Geometric mean | (ref)                                                  | 1.12x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230217-linux-x86_64-iritkatriel-single_arg_exit-3.12.0a5+-b560583 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_pure_python   | 452 us                                                 | 281 us: 1.61x faster                                                   |
| unpickle_pure_python | 302 us                                                 | 196 us: 1.54x faster                                                   |
| json_dumps           | 13.4 ms                                                | 9.33 ms: 1.44x faster                                                  |
| xml_etree_process    | 74.5 ms                                                | 56.2 ms: 1.33x faster                                                  |
| json_loads           | 28.7 us                                                | 23.5 us: 1.22x faster                                                  |
| xml_etree_generate   | 93.8 ms                                                | 80.7 ms: 1.16x faster                                                  |
| pickle_list          | 4.72 us                                                | 4.18 us: 1.13x faster                                                  |
| xml_etree_iterparse  | 111 ms                                                 | 100 ms: 1.11x faster                                                   |
| xml_etree_parse      | 163 ms                                                 | 149 ms: 1.10x faster                                                   |
| unpickle             | 14.2 us                                                | 13.1 us: 1.08x faster                                                  |
| pickle               | 10.2 us                                                | 10.3 us: 1.02x slower                                                  |
| unpickle_list        | 4.92 us                                                | 5.08 us: 1.03x slower                                                  |
| pickle_dict          | 27.6 us                                                | 31.4 us: 1.14x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.18x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230217-linux-x86_64-iritkatriel-single_arg_exit-3.12.0a5+-b560583 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                | 8.97 ms: 1.57x faster                                                  |
| python_startup_no_site | 5.78 ms                                                | 6.50 ms: 1.12x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.18x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230217-linux-x86_64-iritkatriel-single_arg_exit-3.12.0a5+-b560583 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 14.7 ms                                                | 9.89 ms: 1.48x faster                                                  |
| genshi_text     | 30.6 ms                                                | 20.9 ms: 1.46x faster                                                  |
| django_template | 46.3 ms                                                | 33.6 ms: 1.38x faster                                                  |
| genshi_xml      | 63.7 ms                                                | 48.0 ms: 1.33x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.41x faster                                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230217-linux-x86_64-iritkatriel-single_arg_exit-3.12.0a5+-b560583 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| generators              | 76.4 ms                                                | 31.3 ms: 2.44x faster                                                  |
| deltablue               | 7.28 ms                                                | 3.19 ms: 2.28x faster                                                  |
| logging_silent          | 176 ns                                                 | 92.1 ns: 1.92x faster                                                  |
| scimark_sor             | 197 ms                                                 | 107 ms: 1.84x faster                                                   |
| asyncio_tcp             | 914 ms                                                 | 501 ms: 1.83x faster                                                   |
| richards                | 75.2 ms                                                | 42.4 ms: 1.77x faster                                                  |
| go                      | 226 ms                                                 | 134 ms: 1.68x faster                                                   |
| scimark_monte_carlo     | 109 ms                                                 | 64.7 ms: 1.68x faster                                                  |
| pyflate                 | 676 ms                                                 | 408 ms: 1.66x faster                                                   |
| raytrace                | 467 ms                                                 | 283 ms: 1.65x faster                                                   |
| spectral_norm           | 150 ms                                                 | 92.9 ms: 1.61x faster                                                  |
| pickle_pure_python      | 452 us                                                 | 281 us: 1.61x faster                                                   |
| crypto_pyaes            | 117 ms                                                 | 72.6 ms: 1.61x faster                                                  |
| chaos                   | 106 ms                                                 | 66.2 ms: 1.60x faster                                                  |
| python_startup          | 14.1 ms                                                | 8.97 ms: 1.57x faster                                                  |
| hexiom                  | 9.43 ms                                                | 6.10 ms: 1.55x faster                                                  |
| nbody                   | 144 ms                                                 | 93.1 ms: 1.55x faster                                                  |
| unpickle_pure_python    | 302 us                                                 | 196 us: 1.54x faster                                                   |
| deepcopy_memo           | 51.7 us                                                | 34.3 us: 1.51x faster                                                  |
| float                   | 109 ms                                                 | 72.5 ms: 1.50x faster                                                  |
| mako                    | 14.7 ms                                                | 9.89 ms: 1.48x faster                                                  |
| scimark_lu              | 161 ms                                                 | 109 ms: 1.48x faster                                                   |
| genshi_text             | 30.6 ms                                                | 20.9 ms: 1.46x faster                                                  |
| chameleon               | 9.17 ms                                                | 6.29 ms: 1.46x faster                                                  |
| json_dumps              | 13.4 ms                                                | 9.33 ms: 1.44x faster                                                  |
| unpack_sequence         | 59.4 ns                                                | 41.3 ns: 1.44x faster                                                  |
| pprint_pformat          | 1.98 sec                                               | 1.38 sec: 1.43x faster                                                 |
| sqlglot_parse           | 2.04 ms                                                | 1.43 ms: 1.43x faster                                                  |
| pprint_safe_repr        | 953 ms                                                 | 670 ms: 1.42x faster                                                   |
| logging_simple          | 8.10 us                                                | 5.73 us: 1.41x faster                                                  |
| sqlglot_transpile       | 2.43 ms                                                | 1.72 ms: 1.41x faster                                                  |
| logging_format          | 8.85 us                                                | 6.34 us: 1.40x faster                                                  |
| coroutines              | 31.6 ms                                                | 22.7 ms: 1.40x faster                                                  |
| html5lib                | 85.9 ms                                                | 61.7 ms: 1.39x faster                                                  |
| pycparser               | 1.53 sec                                               | 1.10 sec: 1.39x faster                                                 |
| django_template         | 46.3 ms                                                | 33.6 ms: 1.38x faster                                                  |
| scimark_fft             | 421 ms                                                 | 306 ms: 1.38x faster                                                   |
| regex_compile           | 177 ms                                                 | 129 ms: 1.37x faster                                                   |
| thrift                  | 1.03 ms                                                | 759 us: 1.36x faster                                                   |
| 2to3                    | 335 ms                                                 | 246 ms: 1.36x faster                                                   |
| tornado_http            | 128 ms                                                 | 95.2 ms: 1.35x faster                                                  |
| async_tree_io           | 1.78 sec                                               | 1.32 sec: 1.34x faster                                                 |
| async_tree_none         | 711 ms                                                 | 529 ms: 1.34x faster                                                   |
| aiohttp                 | 1.34 ms                                                | 1.00 ms: 1.34x faster                                                  |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.08 ms: 1.34x faster                                                  |
| fannkuch                | 488 ms                                                 | 366 ms: 1.33x faster                                                   |
| genshi_xml              | 63.7 ms                                                | 48.0 ms: 1.33x faster                                                  |
| gunicorn                | 1.43 ms                                                | 1.08 ms: 1.33x faster                                                  |
| xml_etree_process       | 74.5 ms                                                | 56.2 ms: 1.33x faster                                                  |
| mypy2                   | 430 ms                                                 | 329 ms: 1.31x faster                                                   |
| deepcopy                | 438 us                                                 | 335 us: 1.30x faster                                                   |
| deepcopy_reduce         | 3.79 us                                                | 2.93 us: 1.29x faster                                                  |
| sqlglot_normalize       | 134 ms                                                 | 104 ms: 1.29x faster                                                   |
| nqueens                 | 100 ms                                                 | 77.6 ms: 1.29x faster                                                  |
| async_tree_memoization  | 855 ms                                                 | 663 ms: 1.29x faster                                                   |
| sqlglot_optimize        | 65.2 ms                                                | 50.8 ms: 1.28x faster                                                  |
| async_tree_cpu_io_mixed | 949 ms                                                 | 745 ms: 1.27x faster                                                   |
| docutils                | 3.18 sec                                               | 2.54 sec: 1.25x faster                                                 |
| json_loads              | 28.7 us                                                | 23.5 us: 1.22x faster                                                  |
| dulwich_log             | 75.8 ms                                                | 62.6 ms: 1.21x faster                                                  |
| sqlalchemy_declarative  | 165 ms                                                 | 136 ms: 1.21x faster                                                   |
| sympy_integrate         | 24.0 ms                                                | 19.9 ms: 1.21x faster                                                  |
| bench_thread_pool       | 946 us                                                 | 785 us: 1.20x faster                                                   |
| sympy_str               | 325 ms                                                 | 272 ms: 1.19x faster                                                   |
| sqlalchemy_imperative   | 21.5 ms                                                | 18.0 ms: 1.19x faster                                                  |
| json                    | 5.35 ms                                                | 4.55 ms: 1.17x faster                                                  |
| sympy_expand            | 534 ms                                                 | 455 ms: 1.17x faster                                                   |
| regex_v8                | 25.0 ms                                                | 21.3 ms: 1.17x faster                                                  |
| xml_etree_generate      | 93.8 ms                                                | 80.7 ms: 1.16x faster                                                  |
| sympy_sum               | 183 ms                                                 | 158 ms: 1.16x faster                                                   |
| djangocms               | 36.9 us                                                | 32.5 us: 1.13x faster                                                  |
| pickle_list             | 4.72 us                                                | 4.18 us: 1.13x faster                                                  |
| create_gc_cycles        | 1.65 ms                                                | 1.47 ms: 1.12x faster                                                  |
| sqlite_synth            | 2.92 us                                                | 2.63 us: 1.11x faster                                                  |
| xml_etree_iterparse     | 111 ms                                                 | 100 ms: 1.11x faster                                                   |
| meteor_contest          | 114 ms                                                 | 104 ms: 1.10x faster                                                   |
| xml_etree_parse         | 163 ms                                                 | 149 ms: 1.10x faster                                                   |
| pathlib                 | 20.0 ms                                                | 18.4 ms: 1.09x faster                                                  |
| unpickle                | 14.2 us                                                | 13.1 us: 1.08x faster                                                  |
| telco                   | 6.73 ms                                                | 6.29 ms: 1.07x faster                                                  |
| mdp                     | 2.74 sec                                               | 2.62 sec: 1.05x faster                                                 |
| async_generators        | 426 ms                                                 | 412 ms: 1.03x faster                                                   |
| regex_dna               | 214 ms                                                 | 212 ms: 1.01x faster                                                   |
| pidigits                | 190 ms                                                 | 189 ms: 1.00x faster                                                   |
| pickle                  | 10.2 us                                                | 10.3 us: 1.02x slower                                                  |
| regex_effbot            | 3.19 ms                                                | 3.28 ms: 1.03x slower                                                  |
| unpickle_list           | 4.92 us                                                | 5.08 us: 1.03x slower                                                  |
| python_startup_no_site  | 5.78 ms                                                | 6.50 ms: 1.12x slower                                                  |
| pickle_dict             | 27.6 us                                                | 31.4 us: 1.14x slower                                                  |
| dask                    | 436 ms                                                 | 499 ms: 1.14x slower                                                   |
| coverage                | 74.7 ms                                                | 96.4 ms: 1.29x slower                                                  |
| Geometric mean          | (ref)                                                  | 1.31x faster                                                           |

Benchmark hidden because not significant (2): gc_traversal, bench_mp_pool
Ignored benchmarks (2) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, pylint
