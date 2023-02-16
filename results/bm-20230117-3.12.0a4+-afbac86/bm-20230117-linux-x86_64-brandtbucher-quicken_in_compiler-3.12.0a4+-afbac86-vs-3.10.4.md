
# Results vs. 3.10.4

- fork: brandtbucher
- ref: quicken_in_compiler
- machine: linux-x86_64
- commit hash: afbac86
- commit date: 2023-01-17
- overall geometric mean: 1.30x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230117-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-afbac86 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 335 ms                                                 | 252 ms: 1.33x faster                                                        |
| chameleon      | 9.17 ms                                                | 6.39 ms: 1.43x faster                                                       |
| docutils       | 3.18 sec                                               | 2.50 sec: 1.27x faster                                                      |
| html5lib       | 85.9 ms                                                | 60.3 ms: 1.42x faster                                                       |
| tornado_http   | 128 ms                                                 | 93.8 ms: 1.37x faster                                                       |
| Geometric mean | (ref)                                                  | 1.36x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230117-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-afbac86 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 144 ms                                                 | 94.5 ms: 1.52x faster                                                       |
| float          | 109 ms                                                 | 73.0 ms: 1.49x faster                                                       |
| pidigits       | 190 ms                                                 | 189 ms: 1.00x faster                                                        |
| Geometric mean | (ref)                                                  | 1.32x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230117-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-afbac86 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 129 ms: 1.38x faster                                                        |
| regex_v8       | 25.0 ms                                                | 22.4 ms: 1.12x faster                                                       |
| regex_dna      | 214 ms                                                 | 207 ms: 1.03x faster                                                        |
| regex_effbot   | 3.19 ms                                                | 3.48 ms: 1.09x slower                                                       |
| Geometric mean | (ref)                                                  | 1.10x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230117-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-afbac86 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_pure_python   | 452 us                                                 | 288 us: 1.57x faster                                                        |
| unpickle_pure_python | 302 us                                                 | 204 us: 1.48x faster                                                        |
| json_dumps           | 13.4 ms                                                | 9.35 ms: 1.44x faster                                                       |
| xml_etree_process    | 74.5 ms                                                | 54.4 ms: 1.37x faster                                                       |
| xml_etree_generate   | 93.8 ms                                                | 78.0 ms: 1.20x faster                                                       |
| json_loads           | 28.7 us                                                | 24.1 us: 1.19x faster                                                       |
| pickle_list          | 4.72 us                                                | 4.00 us: 1.18x faster                                                       |
| xml_etree_parse      | 163 ms                                                 | 149 ms: 1.09x faster                                                        |
| unpickle             | 14.2 us                                                | 13.2 us: 1.07x faster                                                       |
| xml_etree_iterparse  | 111 ms                                                 | 106 ms: 1.04x faster                                                        |
| pickle               | 10.2 us                                                | 9.93 us: 1.02x faster                                                       |
| unpickle_list        | 4.92 us                                                | 5.06 us: 1.03x slower                                                       |
| pickle_dict          | 27.6 us                                                | 29.9 us: 1.08x slower                                                       |
| Geometric mean       | (ref)                                                  | 1.18x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230117-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-afbac86 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                | 8.89 ms: 1.58x faster                                                       |
| python_startup_no_site | 5.78 ms                                                | 6.42 ms: 1.11x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.19x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230117-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-afbac86 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                | 9.65 ms: 1.52x faster                                                       |
| genshi_text     | 30.6 ms                                                | 20.9 ms: 1.47x faster                                                       |
| django_template | 46.3 ms                                                | 32.0 ms: 1.45x faster                                                       |
| genshi_xml      | 63.7 ms                                                | 47.4 ms: 1.34x faster                                                       |
| Geometric mean  | (ref)                                                  | 1.44x faster                                                                |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230117-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-afbac86 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deltablue               | 7.28 ms                                                | 3.22 ms: 2.26x faster                                                       |
| logging_silent          | 176 ns                                                 | 91.2 ns: 1.93x faster                                                       |
| scimark_sor             | 197 ms                                                 | 107 ms: 1.85x faster                                                        |
| asyncio_tcp             | 914 ms                                                 | 496 ms: 1.84x faster                                                        |
| richards                | 75.2 ms                                                | 43.0 ms: 1.75x faster                                                       |
| pyflate                 | 676 ms                                                 | 404 ms: 1.67x faster                                                        |
| scimark_monte_carlo     | 109 ms                                                 | 65.2 ms: 1.67x faster                                                       |
| chaos                   | 106 ms                                                 | 64.3 ms: 1.64x faster                                                       |
| raytrace                | 467 ms                                                 | 284 ms: 1.64x faster                                                        |
| go                      | 226 ms                                                 | 138 ms: 1.64x faster                                                        |
| spectral_norm           | 150 ms                                                 | 93.8 ms: 1.59x faster                                                       |
| crypto_pyaes            | 117 ms                                                 | 73.2 ms: 1.59x faster                                                       |
| python_startup          | 14.1 ms                                                | 8.89 ms: 1.58x faster                                                       |
| hexiom                  | 9.43 ms                                                | 5.98 ms: 1.58x faster                                                       |
| pickle_pure_python      | 452 us                                                 | 288 us: 1.57x faster                                                        |
| nbody                   | 144 ms                                                 | 94.5 ms: 1.52x faster                                                       |
| mako                    | 14.7 ms                                                | 9.65 ms: 1.52x faster                                                       |
| scimark_lu              | 161 ms                                                 | 107 ms: 1.50x faster                                                        |
| deepcopy_memo           | 51.7 us                                                | 34.5 us: 1.50x faster                                                       |
| float                   | 109 ms                                                 | 73.0 ms: 1.49x faster                                                       |
| unpickle_pure_python    | 302 us                                                 | 204 us: 1.48x faster                                                        |
| genshi_text             | 30.6 ms                                                | 20.9 ms: 1.47x faster                                                       |
| sqlglot_parse           | 2.04 ms                                                | 1.40 ms: 1.46x faster                                                       |
| django_template         | 46.3 ms                                                | 32.0 ms: 1.45x faster                                                       |
| json_dumps              | 13.4 ms                                                | 9.35 ms: 1.44x faster                                                       |
| chameleon               | 9.17 ms                                                | 6.39 ms: 1.43x faster                                                       |
| pprint_pformat          | 1.98 sec                                               | 1.38 sec: 1.43x faster                                                      |
| unpack_sequence         | 59.4 ns                                                | 41.4 ns: 1.43x faster                                                       |
| sqlglot_transpile       | 2.43 ms                                                | 1.70 ms: 1.43x faster                                                       |
| html5lib                | 85.9 ms                                                | 60.3 ms: 1.42x faster                                                       |
| pprint_safe_repr        | 953 ms                                                 | 671 ms: 1.42x faster                                                        |
| thrift                  | 1.03 ms                                                | 739 us: 1.40x faster                                                        |
| logging_simple          | 8.10 us                                                | 5.82 us: 1.39x faster                                                       |
| regex_compile           | 177 ms                                                 | 129 ms: 1.38x faster                                                        |
| scimark_fft             | 421 ms                                                 | 306 ms: 1.38x faster                                                        |
| logging_format          | 8.85 us                                                | 6.45 us: 1.37x faster                                                       |
| xml_etree_process       | 74.5 ms                                                | 54.4 ms: 1.37x faster                                                       |
| tornado_http            | 128 ms                                                 | 93.8 ms: 1.37x faster                                                       |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.00 ms: 1.36x faster                                                       |
| async_tree_none         | 711 ms                                                 | 525 ms: 1.35x faster                                                        |
| async_tree_io           | 1.78 sec                                               | 1.32 sec: 1.34x faster                                                      |
| genshi_xml              | 63.7 ms                                                | 47.4 ms: 1.34x faster                                                       |
| aiohttp                 | 1.34 ms                                                | 1.00 ms: 1.34x faster                                                       |
| deepcopy                | 438 us                                                 | 328 us: 1.33x faster                                                        |
| gunicorn                | 1.43 ms                                                | 1.07 ms: 1.33x faster                                                       |
| pycparser               | 1.53 sec                                               | 1.15 sec: 1.33x faster                                                      |
| 2to3                    | 335 ms                                                 | 252 ms: 1.33x faster                                                        |
| nqueens                 | 100 ms                                                 | 76.6 ms: 1.31x faster                                                       |
| async_tree_memoization  | 855 ms                                                 | 659 ms: 1.30x faster                                                        |
| fannkuch                | 488 ms                                                 | 376 ms: 1.30x faster                                                        |
| deepcopy_reduce         | 3.79 us                                                | 2.95 us: 1.29x faster                                                       |
| sqlglot_normalize       | 134 ms                                                 | 105 ms: 1.28x faster                                                        |
| sqlglot_optimize        | 65.2 ms                                                | 51.0 ms: 1.28x faster                                                       |
| coroutines              | 31.6 ms                                                | 24.8 ms: 1.27x faster                                                       |
| docutils                | 3.18 sec                                               | 2.50 sec: 1.27x faster                                                      |
| async_tree_cpu_io_mixed | 949 ms                                                 | 752 ms: 1.26x faster                                                        |
| dulwich_log             | 75.8 ms                                                | 62.2 ms: 1.22x faster                                                       |
| bench_thread_pool       | 946 us                                                 | 778 us: 1.22x faster                                                        |
| sympy_integrate         | 24.0 ms                                                | 19.8 ms: 1.21x faster                                                       |
| sympy_str               | 325 ms                                                 | 269 ms: 1.21x faster                                                        |
| async_generators        | 426 ms                                                 | 354 ms: 1.20x faster                                                        |
| xml_etree_generate      | 93.8 ms                                                | 78.0 ms: 1.20x faster                                                       |
| json_loads              | 28.7 us                                                | 24.1 us: 1.19x faster                                                       |
| pickle_list             | 4.72 us                                                | 4.00 us: 1.18x faster                                                       |
| sympy_sum               | 183 ms                                                 | 155 ms: 1.18x faster                                                        |
| sympy_expand            | 534 ms                                                 | 454 ms: 1.17x faster                                                        |
| json                    | 5.35 ms                                                | 4.66 ms: 1.15x faster                                                       |
| djangocms               | 36.9 us                                                | 32.3 us: 1.14x faster                                                       |
| sqlite_synth            | 2.92 us                                                | 2.56 us: 1.14x faster                                                       |
| pathlib                 | 20.0 ms                                                | 17.7 ms: 1.13x faster                                                       |
| create_gc_cycles        | 1.65 ms                                                | 1.47 ms: 1.12x faster                                                       |
| regex_v8                | 25.0 ms                                                | 22.4 ms: 1.12x faster                                                       |
| xml_etree_parse         | 163 ms                                                 | 149 ms: 1.09x faster                                                        |
| meteor_contest          | 114 ms                                                 | 104 ms: 1.09x faster                                                        |
| unpickle                | 14.2 us                                                | 13.2 us: 1.07x faster                                                       |
| mdp                     | 2.74 sec                                               | 2.56 sec: 1.07x faster                                                      |
| telco                   | 6.73 ms                                                | 6.35 ms: 1.06x faster                                                       |
| xml_etree_iterparse     | 111 ms                                                 | 106 ms: 1.04x faster                                                        |
| regex_dna               | 214 ms                                                 | 207 ms: 1.03x faster                                                        |
| pickle                  | 10.2 us                                                | 9.93 us: 1.02x faster                                                       |
| pidigits                | 190 ms                                                 | 189 ms: 1.00x faster                                                        |
| generators              | 76.4 ms                                                | 76.6 ms: 1.00x slower                                                       |
| unpickle_list           | 4.92 us                                                | 5.06 us: 1.03x slower                                                       |
| pickle_dict             | 27.6 us                                                | 29.9 us: 1.08x slower                                                       |
| regex_effbot            | 3.19 ms                                                | 3.48 ms: 1.09x slower                                                       |
| python_startup_no_site  | 5.78 ms                                                | 6.42 ms: 1.11x slower                                                       |
| dask                    | 436 ms                                                 | 497 ms: 1.14x slower                                                        |
| gc_traversal            | 3.53 ms                                                | 4.29 ms: 1.22x slower                                                       |
| coverage                | 74.7 ms                                                | 93.1 ms: 1.25x slower                                                       |
| Geometric mean          | (ref)                                                  | 1.30x faster                                                                |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230117-3.12.0a4+-afbac86/bm-20230117-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-afbac86.json: mypy
