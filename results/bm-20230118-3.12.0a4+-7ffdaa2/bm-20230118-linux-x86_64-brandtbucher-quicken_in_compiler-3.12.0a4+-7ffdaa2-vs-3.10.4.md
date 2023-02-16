
# Results vs. 3.10.4

- fork: brandtbucher
- ref: quicken_in_compiler
- machine: linux-x86_64
- commit hash: 7ffdaa2
- commit date: 2023-01-18
- overall geometric mean: 1.30x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230118-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-7ffdaa2 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 335 ms                                                 | 250 ms: 1.34x faster                                                        |
| chameleon      | 9.17 ms                                                | 6.28 ms: 1.46x faster                                                       |
| docutils       | 3.18 sec                                               | 2.52 sec: 1.26x faster                                                      |
| html5lib       | 85.9 ms                                                | 59.7 ms: 1.44x faster                                                       |
| tornado_http   | 128 ms                                                 | 93.9 ms: 1.37x faster                                                       |
| Geometric mean | (ref)                                                  | 1.37x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230118-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-7ffdaa2 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 144 ms                                                 | 93.9 ms: 1.53x faster                                                       |
| float          | 109 ms                                                 | 72.0 ms: 1.51x faster                                                       |
| pidigits       | 190 ms                                                 | 198 ms: 1.04x slower                                                        |
| Geometric mean | (ref)                                                  | 1.31x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230118-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-7ffdaa2 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 128 ms: 1.38x faster                                                        |
| regex_v8       | 25.0 ms                                                | 21.8 ms: 1.15x faster                                                       |
| regex_dna      | 214 ms                                                 | 208 ms: 1.03x faster                                                        |
| regex_effbot   | 3.19 ms                                                | 3.44 ms: 1.08x slower                                                       |
| Geometric mean | (ref)                                                  | 1.11x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230118-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-7ffdaa2 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_pure_python   | 452 us                                                 | 280 us: 1.61x faster                                                        |
| unpickle_pure_python | 302 us                                                 | 196 us: 1.53x faster                                                        |
| json_dumps           | 13.4 ms                                                | 9.45 ms: 1.42x faster                                                       |
| xml_etree_process    | 74.5 ms                                                | 54.0 ms: 1.38x faster                                                       |
| xml_etree_generate   | 93.8 ms                                                | 77.9 ms: 1.20x faster                                                       |
| json_loads           | 28.7 us                                                | 24.0 us: 1.19x faster                                                       |
| pickle_list          | 4.72 us                                                | 4.04 us: 1.17x faster                                                       |
| xml_etree_parse      | 163 ms                                                 | 147 ms: 1.11x faster                                                        |
| unpickle             | 14.2 us                                                | 13.3 us: 1.07x faster                                                       |
| xml_etree_iterparse  | 111 ms                                                 | 105 ms: 1.06x faster                                                        |
| pickle               | 10.2 us                                                | 10.1 us: 1.01x faster                                                       |
| unpickle_list        | 4.92 us                                                | 5.11 us: 1.04x slower                                                       |
| pickle_dict          | 27.6 us                                                | 31.0 us: 1.12x slower                                                       |
| Geometric mean       | (ref)                                                  | 1.18x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230118-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-7ffdaa2 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                | 8.84 ms: 1.59x faster                                                       |
| python_startup_no_site | 5.78 ms                                                | 6.39 ms: 1.11x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.20x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230118-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-7ffdaa2 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 30.6 ms                                                | 20.3 ms: 1.51x faster                                                       |
| mako            | 14.7 ms                                                | 9.75 ms: 1.50x faster                                                       |
| django_template | 46.3 ms                                                | 32.5 ms: 1.42x faster                                                       |
| genshi_xml      | 63.7 ms                                                | 46.6 ms: 1.37x faster                                                       |
| Geometric mean  | (ref)                                                  | 1.45x faster                                                                |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230118-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-7ffdaa2 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deltablue               | 7.28 ms                                                | 3.28 ms: 2.22x faster                                                       |
| logging_silent          | 176 ns                                                 | 92.1 ns: 1.92x faster                                                       |
| scimark_sor             | 197 ms                                                 | 104 ms: 1.89x faster                                                        |
| asyncio_tcp             | 914 ms                                                 | 489 ms: 1.87x faster                                                        |
| richards                | 75.2 ms                                                | 42.1 ms: 1.78x faster                                                       |
| pyflate                 | 676 ms                                                 | 391 ms: 1.73x faster                                                        |
| go                      | 226 ms                                                 | 134 ms: 1.69x faster                                                        |
| raytrace                | 467 ms                                                 | 280 ms: 1.67x faster                                                        |
| scimark_monte_carlo     | 109 ms                                                 | 66.0 ms: 1.64x faster                                                       |
| chaos                   | 106 ms                                                 | 64.4 ms: 1.64x faster                                                       |
| pickle_pure_python      | 452 us                                                 | 280 us: 1.61x faster                                                        |
| python_startup          | 14.1 ms                                                | 8.84 ms: 1.59x faster                                                       |
| crypto_pyaes            | 117 ms                                                 | 73.2 ms: 1.59x faster                                                       |
| spectral_norm           | 150 ms                                                 | 94.4 ms: 1.58x faster                                                       |
| hexiom                  | 9.43 ms                                                | 5.95 ms: 1.58x faster                                                       |
| unpickle_pure_python    | 302 us                                                 | 196 us: 1.53x faster                                                        |
| nbody                   | 144 ms                                                 | 93.9 ms: 1.53x faster                                                       |
| float                   | 109 ms                                                 | 72.0 ms: 1.51x faster                                                       |
| genshi_text             | 30.6 ms                                                | 20.3 ms: 1.51x faster                                                       |
| mako                    | 14.7 ms                                                | 9.75 ms: 1.50x faster                                                       |
| scimark_lu              | 161 ms                                                 | 107 ms: 1.50x faster                                                        |
| deepcopy_memo           | 51.7 us                                                | 34.5 us: 1.50x faster                                                       |
| chameleon               | 9.17 ms                                                | 6.28 ms: 1.46x faster                                                       |
| sqlglot_parse           | 2.04 ms                                                | 1.40 ms: 1.46x faster                                                       |
| html5lib                | 85.9 ms                                                | 59.7 ms: 1.44x faster                                                       |
| sqlglot_transpile       | 2.43 ms                                                | 1.69 ms: 1.44x faster                                                       |
| django_template         | 46.3 ms                                                | 32.5 ms: 1.42x faster                                                       |
| json_dumps              | 13.4 ms                                                | 9.45 ms: 1.42x faster                                                       |
| scimark_fft             | 421 ms                                                 | 296 ms: 1.42x faster                                                        |
| pprint_pformat          | 1.98 sec                                               | 1.41 sec: 1.41x faster                                                      |
| logging_simple          | 8.10 us                                                | 5.77 us: 1.40x faster                                                       |
| logging_format          | 8.85 us                                                | 6.37 us: 1.39x faster                                                       |
| scimark_sparse_mat_mult | 5.45 ms                                                | 3.93 ms: 1.39x faster                                                       |
| thrift                  | 1.03 ms                                                | 747 us: 1.39x faster                                                        |
| regex_compile           | 177 ms                                                 | 128 ms: 1.38x faster                                                        |
| xml_etree_process       | 74.5 ms                                                | 54.0 ms: 1.38x faster                                                       |
| pycparser               | 1.53 sec                                               | 1.12 sec: 1.37x faster                                                      |
| pprint_safe_repr        | 953 ms                                                 | 696 ms: 1.37x faster                                                        |
| genshi_xml              | 63.7 ms                                                | 46.6 ms: 1.37x faster                                                       |
| tornado_http            | 128 ms                                                 | 93.9 ms: 1.37x faster                                                       |
| async_tree_none         | 711 ms                                                 | 525 ms: 1.35x faster                                                        |
| aiohttp                 | 1.34 ms                                                | 992 us: 1.35x faster                                                        |
| async_tree_io           | 1.78 sec                                               | 1.32 sec: 1.35x faster                                                      |
| 2to3                    | 335 ms                                                 | 250 ms: 1.34x faster                                                        |
| unpack_sequence         | 59.4 ns                                                | 44.3 ns: 1.34x faster                                                       |
| gunicorn                | 1.43 ms                                                | 1.07 ms: 1.34x faster                                                       |
| deepcopy                | 438 us                                                 | 332 us: 1.32x faster                                                        |
| fannkuch                | 488 ms                                                 | 371 ms: 1.32x faster                                                        |
| nqueens                 | 100 ms                                                 | 76.3 ms: 1.31x faster                                                       |
| async_tree_memoization  | 855 ms                                                 | 653 ms: 1.31x faster                                                        |
| sqlglot_normalize       | 134 ms                                                 | 105 ms: 1.28x faster                                                        |
| coroutines              | 31.6 ms                                                | 24.6 ms: 1.28x faster                                                       |
| sqlglot_optimize        | 65.2 ms                                                | 51.0 ms: 1.28x faster                                                       |
| deepcopy_reduce         | 3.79 us                                                | 2.96 us: 1.28x faster                                                       |
| docutils                | 3.18 sec                                               | 2.52 sec: 1.26x faster                                                      |
| async_tree_cpu_io_mixed | 949 ms                                                 | 755 ms: 1.26x faster                                                        |
| dulwich_log             | 75.8 ms                                                | 62.1 ms: 1.22x faster                                                       |
| sympy_integrate         | 24.0 ms                                                | 19.7 ms: 1.22x faster                                                       |
| bench_thread_pool       | 946 us                                                 | 780 us: 1.21x faster                                                        |
| async_generators        | 426 ms                                                 | 351 ms: 1.21x faster                                                        |
| sympy_str               | 325 ms                                                 | 269 ms: 1.21x faster                                                        |
| xml_etree_generate      | 93.8 ms                                                | 77.9 ms: 1.20x faster                                                       |
| json_loads              | 28.7 us                                                | 24.0 us: 1.19x faster                                                       |
| sympy_expand            | 534 ms                                                 | 452 ms: 1.18x faster                                                        |
| sympy_sum               | 183 ms                                                 | 156 ms: 1.18x faster                                                        |
| json                    | 5.35 ms                                                | 4.58 ms: 1.17x faster                                                       |
| pickle_list             | 4.72 us                                                | 4.04 us: 1.17x faster                                                       |
| regex_v8                | 25.0 ms                                                | 21.8 ms: 1.15x faster                                                       |
| create_gc_cycles        | 1.65 ms                                                | 1.44 ms: 1.15x faster                                                       |
| pathlib                 | 20.0 ms                                                | 17.5 ms: 1.14x faster                                                       |
| sqlite_synth            | 2.92 us                                                | 2.57 us: 1.14x faster                                                       |
| djangocms               | 36.9 us                                                | 32.5 us: 1.13x faster                                                       |
| meteor_contest          | 114 ms                                                 | 103 ms: 1.11x faster                                                        |
| xml_etree_parse         | 163 ms                                                 | 147 ms: 1.11x faster                                                        |
| unpickle                | 14.2 us                                                | 13.3 us: 1.07x faster                                                       |
| xml_etree_iterparse     | 111 ms                                                 | 105 ms: 1.06x faster                                                        |
| telco                   | 6.73 ms                                                | 6.37 ms: 1.06x faster                                                       |
| mdp                     | 2.74 sec                                               | 2.66 sec: 1.03x faster                                                      |
| regex_dna               | 214 ms                                                 | 208 ms: 1.03x faster                                                        |
| generators              | 76.4 ms                                                | 75.0 ms: 1.02x faster                                                       |
| pickle                  | 10.2 us                                                | 10.1 us: 1.01x faster                                                       |
| unpickle_list           | 4.92 us                                                | 5.11 us: 1.04x slower                                                       |
| pidigits                | 190 ms                                                 | 198 ms: 1.04x slower                                                        |
| regex_effbot            | 3.19 ms                                                | 3.44 ms: 1.08x slower                                                       |
| gc_traversal            | 3.53 ms                                                | 3.81 ms: 1.08x slower                                                       |
| python_startup_no_site  | 5.78 ms                                                | 6.39 ms: 1.11x slower                                                       |
| pickle_dict             | 27.6 us                                                | 31.0 us: 1.12x slower                                                       |
| dask                    | 436 ms                                                 | 492 ms: 1.13x slower                                                        |
| coverage                | 74.7 ms                                                | 95.3 ms: 1.28x slower                                                       |
| Geometric mean          | (ref)                                                  | 1.30x faster                                                                |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230118-3.12.0a4+-7ffdaa2/bm-20230118-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-7ffdaa2.json: mypy
