
# Results vs. 3.10.4

- fork: brandtbucher
- ref: quicken_in_compiler
- machine: linux-x86_64
- commit hash: 933012e
- commit date: 2023-01-18
- overall geometric mean: 1.31x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230118-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-933012e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 335 ms                                                 | 249 ms: 1.35x faster                                                        |
| chameleon      | 9.17 ms                                                | 6.37 ms: 1.44x faster                                                       |
| docutils       | 3.18 sec                                               | 2.48 sec: 1.28x faster                                                      |
| html5lib       | 85.9 ms                                                | 59.8 ms: 1.44x faster                                                       |
| tornado_http   | 128 ms                                                 | 94.3 ms: 1.36x faster                                                       |
| Geometric mean | (ref)                                                  | 1.37x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230118-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-933012e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 144 ms                                                 | 94.1 ms: 1.53x faster                                                       |
| float          | 109 ms                                                 | 72.3 ms: 1.51x faster                                                       |
| pidigits       | 190 ms                                                 | 189 ms: 1.00x faster                                                        |
| Geometric mean | (ref)                                                  | 1.32x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230118-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-933012e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 128 ms: 1.39x faster                                                        |
| regex_v8       | 25.0 ms                                                | 21.2 ms: 1.18x faster                                                       |
| regex_dna      | 214 ms                                                 | 207 ms: 1.03x faster                                                        |
| regex_effbot   | 3.19 ms                                                | 3.51 ms: 1.10x slower                                                       |
| Geometric mean | (ref)                                                  | 1.11x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230118-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-933012e |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_pure_python   | 452 us                                                 | 280 us: 1.62x faster                                                        |
| unpickle_pure_python | 302 us                                                 | 196 us: 1.54x faster                                                        |
| json_dumps           | 13.4 ms                                                | 9.32 ms: 1.44x faster                                                       |
| xml_etree_process    | 74.5 ms                                                | 54.1 ms: 1.38x faster                                                       |
| xml_etree_generate   | 93.8 ms                                                | 78.5 ms: 1.20x faster                                                       |
| json_loads           | 28.7 us                                                | 24.1 us: 1.19x faster                                                       |
| pickle_list          | 4.72 us                                                | 4.21 us: 1.12x faster                                                       |
| xml_etree_parse      | 163 ms                                                 | 148 ms: 1.10x faster                                                        |
| xml_etree_iterparse  | 111 ms                                                 | 102 ms: 1.09x faster                                                        |
| pickle               | 10.2 us                                                | 10.2 us: 1.01x slower                                                       |
| unpickle_list        | 4.92 us                                                | 5.09 us: 1.03x slower                                                       |
| pickle_dict          | 27.6 us                                                | 31.6 us: 1.15x slower                                                       |
| Geometric mean       | (ref)                                                  | 1.17x faster                                                                |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230118-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-933012e |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                | 8.85 ms: 1.59x faster                                                       |
| python_startup_no_site | 5.78 ms                                                | 6.39 ms: 1.11x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.20x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230118-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-933012e |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                | 9.50 ms: 1.54x faster                                                       |
| genshi_text     | 30.6 ms                                                | 20.0 ms: 1.53x faster                                                       |
| django_template | 46.3 ms                                                | 32.3 ms: 1.44x faster                                                       |
| genshi_xml      | 63.7 ms                                                | 46.0 ms: 1.38x faster                                                       |
| Geometric mean  | (ref)                                                  | 1.47x faster                                                                |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230118-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-933012e |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deltablue               | 7.28 ms                                                | 3.20 ms: 2.28x faster                                                       |
| logging_silent          | 176 ns                                                 | 90.4 ns: 1.95x faster                                                       |
| scimark_sor             | 197 ms                                                 | 105 ms: 1.88x faster                                                        |
| asyncio_tcp             | 914 ms                                                 | 497 ms: 1.84x faster                                                        |
| richards                | 75.2 ms                                                | 42.2 ms: 1.78x faster                                                       |
| pyflate                 | 676 ms                                                 | 399 ms: 1.69x faster                                                        |
| go                      | 226 ms                                                 | 134 ms: 1.69x faster                                                        |
| chaos                   | 106 ms                                                 | 63.3 ms: 1.67x faster                                                       |
| raytrace                | 467 ms                                                 | 283 ms: 1.65x faster                                                        |
| scimark_monte_carlo     | 109 ms                                                 | 65.9 ms: 1.65x faster                                                       |
| pickle_pure_python      | 452 us                                                 | 280 us: 1.62x faster                                                        |
| python_startup          | 14.1 ms                                                | 8.85 ms: 1.59x faster                                                       |
| hexiom                  | 9.43 ms                                                | 5.96 ms: 1.58x faster                                                       |
| crypto_pyaes            | 117 ms                                                 | 74.1 ms: 1.57x faster                                                       |
| mako                    | 14.7 ms                                                | 9.50 ms: 1.54x faster                                                       |
| unpickle_pure_python    | 302 us                                                 | 196 us: 1.54x faster                                                        |
| spectral_norm           | 150 ms                                                 | 97.4 ms: 1.54x faster                                                       |
| nbody                   | 144 ms                                                 | 94.1 ms: 1.53x faster                                                       |
| genshi_text             | 30.6 ms                                                | 20.0 ms: 1.53x faster                                                       |
| scimark_lu              | 161 ms                                                 | 106 ms: 1.52x faster                                                        |
| float                   | 109 ms                                                 | 72.3 ms: 1.51x faster                                                       |
| deepcopy_memo           | 51.7 us                                                | 34.4 us: 1.50x faster                                                       |
| sqlglot_parse           | 2.04 ms                                                | 1.41 ms: 1.45x faster                                                       |
| pprint_pformat          | 1.98 sec                                               | 1.37 sec: 1.44x faster                                                      |
| json_dumps              | 13.4 ms                                                | 9.32 ms: 1.44x faster                                                       |
| logging_simple          | 8.10 us                                                | 5.62 us: 1.44x faster                                                       |
| chameleon               | 9.17 ms                                                | 6.37 ms: 1.44x faster                                                       |
| html5lib                | 85.9 ms                                                | 59.8 ms: 1.44x faster                                                       |
| django_template         | 46.3 ms                                                | 32.3 ms: 1.44x faster                                                       |
| logging_format          | 8.85 us                                                | 6.18 us: 1.43x faster                                                       |
| sqlglot_transpile       | 2.43 ms                                                | 1.70 ms: 1.43x faster                                                       |
| pprint_safe_repr        | 953 ms                                                 | 670 ms: 1.42x faster                                                        |
| pycparser               | 1.53 sec                                               | 1.08 sec: 1.42x faster                                                      |
| thrift                  | 1.03 ms                                                | 739 us: 1.40x faster                                                        |
| scimark_fft             | 421 ms                                                 | 301 ms: 1.40x faster                                                        |
| regex_compile           | 177 ms                                                 | 128 ms: 1.39x faster                                                        |
| genshi_xml              | 63.7 ms                                                | 46.0 ms: 1.38x faster                                                       |
| xml_etree_process       | 74.5 ms                                                | 54.1 ms: 1.38x faster                                                       |
| scimark_sparse_mat_mult | 5.45 ms                                                | 3.96 ms: 1.38x faster                                                       |
| tornado_http            | 128 ms                                                 | 94.3 ms: 1.36x faster                                                       |
| aiohttp                 | 1.34 ms                                                | 991 us: 1.35x faster                                                        |
| async_tree_none         | 711 ms                                                 | 527 ms: 1.35x faster                                                        |
| unpack_sequence         | 59.4 ns                                                | 44.0 ns: 1.35x faster                                                       |
| gunicorn                | 1.43 ms                                                | 1.06 ms: 1.35x faster                                                       |
| fannkuch                | 488 ms                                                 | 362 ms: 1.35x faster                                                        |
| 2to3                    | 335 ms                                                 | 249 ms: 1.35x faster                                                        |
| deepcopy                | 438 us                                                 | 325 us: 1.35x faster                                                        |
| async_tree_io           | 1.78 sec                                               | 1.32 sec: 1.34x faster                                                      |
| async_tree_memoization  | 855 ms                                                 | 639 ms: 1.34x faster                                                        |
| deepcopy_reduce         | 3.79 us                                                | 2.92 us: 1.30x faster                                                       |
| nqueens                 | 100 ms                                                 | 77.2 ms: 1.30x faster                                                       |
| docutils                | 3.18 sec                                               | 2.48 sec: 1.28x faster                                                      |
| sqlglot_optimize        | 65.2 ms                                                | 51.4 ms: 1.27x faster                                                       |
| sqlglot_normalize       | 134 ms                                                 | 106 ms: 1.26x faster                                                        |
| async_tree_cpu_io_mixed | 949 ms                                                 | 751 ms: 1.26x faster                                                        |
| sympy_integrate         | 24.0 ms                                                | 19.7 ms: 1.22x faster                                                       |
| async_generators        | 426 ms                                                 | 349 ms: 1.22x faster                                                        |
| coroutines              | 31.6 ms                                                | 26.0 ms: 1.22x faster                                                       |
| bench_thread_pool       | 946 us                                                 | 779 us: 1.21x faster                                                        |
| dulwich_log             | 75.8 ms                                                | 62.9 ms: 1.20x faster                                                       |
| sympy_str               | 325 ms                                                 | 270 ms: 1.20x faster                                                        |
| xml_etree_generate      | 93.8 ms                                                | 78.5 ms: 1.20x faster                                                       |
| json_loads              | 28.7 us                                                | 24.1 us: 1.19x faster                                                       |
| sympy_sum               | 183 ms                                                 | 155 ms: 1.18x faster                                                        |
| regex_v8                | 25.0 ms                                                | 21.2 ms: 1.18x faster                                                       |
| sympy_expand            | 534 ms                                                 | 453 ms: 1.18x faster                                                        |
| djangocms               | 36.9 us                                                | 31.9 us: 1.15x faster                                                       |
| json                    | 5.35 ms                                                | 4.64 ms: 1.15x faster                                                       |
| pathlib                 | 20.0 ms                                                | 17.7 ms: 1.13x faster                                                       |
| sqlite_synth            | 2.92 us                                                | 2.59 us: 1.13x faster                                                       |
| create_gc_cycles        | 1.65 ms                                                | 1.46 ms: 1.13x faster                                                       |
| mdp                     | 2.74 sec                                               | 2.44 sec: 1.12x faster                                                      |
| pickle_list             | 4.72 us                                                | 4.21 us: 1.12x faster                                                       |
| meteor_contest          | 114 ms                                                 | 103 ms: 1.11x faster                                                        |
| xml_etree_parse         | 163 ms                                                 | 148 ms: 1.10x faster                                                        |
| xml_etree_iterparse     | 111 ms                                                 | 102 ms: 1.09x faster                                                        |
| telco                   | 6.73 ms                                                | 6.42 ms: 1.05x faster                                                       |
| regex_dna               | 214 ms                                                 | 207 ms: 1.03x faster                                                        |
| generators              | 76.4 ms                                                | 76.0 ms: 1.00x faster                                                       |
| gc_traversal            | 3.53 ms                                                | 3.51 ms: 1.00x faster                                                       |
| pidigits                | 190 ms                                                 | 189 ms: 1.00x faster                                                        |
| pickle                  | 10.2 us                                                | 10.2 us: 1.01x slower                                                       |
| unpickle_list           | 4.92 us                                                | 5.09 us: 1.03x slower                                                       |
| regex_effbot            | 3.19 ms                                                | 3.51 ms: 1.10x slower                                                       |
| python_startup_no_site  | 5.78 ms                                                | 6.39 ms: 1.11x slower                                                       |
| dask                    | 436 ms                                                 | 496 ms: 1.14x slower                                                        |
| pickle_dict             | 27.6 us                                                | 31.6 us: 1.15x slower                                                       |
| coverage                | 74.7 ms                                                | 96.1 ms: 1.29x slower                                                       |
| Geometric mean          | (ref)                                                  | 1.31x faster                                                                |

Benchmark hidden because not significant (2): unpickle, bench_mp_pool
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230118-3.12.0a4+-933012e/bm-20230118-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-933012e.json: mypy
