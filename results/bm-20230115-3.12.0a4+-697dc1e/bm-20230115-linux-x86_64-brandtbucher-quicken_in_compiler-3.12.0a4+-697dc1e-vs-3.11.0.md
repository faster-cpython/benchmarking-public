
# Results vs. 3.11.0

- fork: brandtbucher
- ref: quicken_in_compiler
- machine: linux-x86_64
- commit hash: 697dc1e
- commit date: 2023-01-15
- overall geometric mean: 1.04x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230115-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-697dc1e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 251 ms: 1.03x faster                                                        |
| docutils       | 2.60 sec                                               | 2.48 sec: 1.05x faster                                                      |
| html5lib       | 64.8 ms                                                | 60.4 ms: 1.07x faster                                                       |
| tornado_http   | 96.5 ms                                                | 93.8 ms: 1.03x faster                                                       |
| Geometric mean | (ref)                                                  | 1.04x faster                                                                |

Benchmark hidden because not significant (1): chameleon

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230115-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-697dc1e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 76.8 ms                                                | 71.5 ms: 1.07x faster                                                       |
| pidigits       | 197 ms                                                 | 189 ms: 1.04x faster                                                        |
| nbody          | 90.0 ms                                                | 94.8 ms: 1.05x slower                                                       |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230115-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-697dc1e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 128 ms: 1.06x faster                                                        |
| regex_v8       | 22.2 ms                                                | 21.7 ms: 1.03x faster                                                       |
| regex_effbot   | 3.46 ms                                                | 3.51 ms: 1.02x slower                                                       |
| regex_dna      | 203 ms                                                 | 211 ms: 1.04x slower                                                        |
| Geometric mean | (ref)                                                  | 1.01x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230115-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-697dc1e |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 12.4 ms                                                | 9.34 ms: 1.32x faster                                                       |
| unpickle_pure_python | 227 us                                                 | 196 us: 1.16x faster                                                        |
| pickle_pure_python   | 308 us                                                 | 279 us: 1.10x faster                                                        |
| json_loads           | 26.1 us                                                | 23.9 us: 1.09x faster                                                       |
| pickle_dict          | 31.2 us                                                | 29.9 us: 1.04x faster                                                       |
| xml_etree_parse      | 160 ms                                                 | 157 ms: 1.02x faster                                                        |
| pickle_list          | 4.14 us                                                | 4.06 us: 1.02x faster                                                       |
| xml_etree_process    | 53.7 ms                                                | 54.1 ms: 1.01x slower                                                       |
| pickle               | 9.90 us                                                | 10.2 us: 1.03x slower                                                       |
| xml_etree_generate   | 75.9 ms                                                | 78.8 ms: 1.04x slower                                                       |
| xml_etree_iterparse  | 104 ms                                                 | 109 ms: 1.05x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                                |

Benchmark hidden because not significant (2): unpickle, unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230115-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-697dc1e |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 8.58 ms                                                | 8.68 ms: 1.01x slower                                                       |
| python_startup_no_site | 6.04 ms                                                | 6.22 ms: 1.03x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230115-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-697dc1e |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_xml      | 51.4 ms                                                | 46.1 ms: 1.12x faster                                                       |
| genshi_text     | 21.5 ms                                                | 20.1 ms: 1.07x faster                                                       |
| mako            | 9.83 ms                                                | 9.63 ms: 1.02x faster                                                       |
| django_template | 32.3 ms                                                | 32.0 ms: 1.01x faster                                                       |
| Geometric mean  | (ref)                                                  | 1.05x faster                                                                |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230115-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-697dc1e |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| asyncio_tcp             | 883 ms                                                 | 485 ms: 1.82x faster                                                        |
| json_dumps              | 12.4 ms                                                | 9.34 ms: 1.32x faster                                                       |
| unpickle_pure_python    | 227 us                                                 | 196 us: 1.16x faster                                                        |
| deltablue               | 3.66 ms                                                | 3.19 ms: 1.15x faster                                                       |
| genshi_xml              | 51.4 ms                                                | 46.1 ms: 1.12x faster                                                       |
| pickle_pure_python      | 308 us                                                 | 279 us: 1.10x faster                                                        |
| richards                | 46.1 ms                                                | 42.0 ms: 1.10x faster                                                       |
| json_loads              | 26.1 us                                                | 23.9 us: 1.09x faster                                                       |
| scimark_sor             | 115 ms                                                 | 106 ms: 1.09x faster                                                        |
| float                   | 76.8 ms                                                | 71.5 ms: 1.07x faster                                                       |
| html5lib                | 64.8 ms                                                | 60.4 ms: 1.07x faster                                                       |
| genshi_text             | 21.5 ms                                                | 20.1 ms: 1.07x faster                                                       |
| go                      | 140 ms                                                 | 131 ms: 1.07x faster                                                        |
| pycparser               | 1.19 sec                                               | 1.11 sec: 1.07x faster                                                      |
| nqueens                 | 83.8 ms                                                | 78.5 ms: 1.07x faster                                                       |
| logging_simple          | 6.02 us                                                | 5.65 us: 1.06x faster                                                       |
| regex_compile           | 136 ms                                                 | 128 ms: 1.06x faster                                                        |
| fannkuch                | 384 ms                                                 | 362 ms: 1.06x faster                                                        |
| mdp                     | 2.63 sec                                               | 2.47 sec: 1.06x faster                                                      |
| json                    | 4.87 ms                                                | 4.59 ms: 1.06x faster                                                       |
| scimark_fft             | 325 ms                                                 | 308 ms: 1.06x faster                                                        |
| bench_thread_pool       | 817 us                                                 | 774 us: 1.06x faster                                                        |
| deepcopy                | 341 us                                                 | 324 us: 1.05x faster                                                        |
| pprint_safe_repr        | 706 ms                                                 | 670 ms: 1.05x faster                                                        |
| sympy_expand            | 475 ms                                                 | 452 ms: 1.05x faster                                                        |
| hexiom                  | 6.34 ms                                                | 6.03 ms: 1.05x faster                                                       |
| coroutines              | 26.2 ms                                                | 24.9 ms: 1.05x faster                                                       |
| aiohttp                 | 1.05 ms                                                | 999 us: 1.05x faster                                                        |
| pprint_pformat          | 1.46 sec                                               | 1.39 sec: 1.05x faster                                                      |
| sqlglot_optimize        | 52.7 ms                                                | 50.2 ms: 1.05x faster                                                       |
| chaos                   | 68.7 ms                                                | 65.5 ms: 1.05x faster                                                       |
| create_gc_cycles        | 1.52 ms                                                | 1.45 ms: 1.05x faster                                                       |
| docutils                | 2.60 sec                                               | 2.48 sec: 1.05x faster                                                      |
| logging_silent          | 98.0 ns                                                | 93.8 ns: 1.05x faster                                                       |
| deepcopy_reduce         | 3.02 us                                                | 2.89 us: 1.04x faster                                                       |
| deepcopy_memo           | 35.8 us                                                | 34.4 us: 1.04x faster                                                       |
| pickle_dict             | 31.2 us                                                | 29.9 us: 1.04x faster                                                       |
| pidigits                | 197 ms                                                 | 189 ms: 1.04x faster                                                        |
| sqlglot_normalize       | 108 ms                                                 | 103 ms: 1.04x faster                                                        |
| sympy_integrate         | 21.0 ms                                                | 20.2 ms: 1.04x faster                                                       |
| sympy_str               | 291 ms                                                 | 281 ms: 1.04x faster                                                        |
| pyflate                 | 419 ms                                                 | 404 ms: 1.04x faster                                                        |
| logging_format          | 6.48 us                                                | 6.26 us: 1.03x faster                                                       |
| gunicorn                | 1.12 ms                                                | 1.08 ms: 1.03x faster                                                       |
| 2to3                    | 259 ms                                                 | 251 ms: 1.03x faster                                                        |
| coverage                | 99.3 ms                                                | 96.0 ms: 1.03x faster                                                       |
| crypto_pyaes            | 75.7 ms                                                | 73.3 ms: 1.03x faster                                                       |
| dulwich_log             | 64.0 ms                                                | 62.1 ms: 1.03x faster                                                       |
| tornado_http            | 96.5 ms                                                | 93.8 ms: 1.03x faster                                                       |
| raytrace                | 291 ms                                                 | 283 ms: 1.03x faster                                                        |
| regex_v8                | 22.2 ms                                                | 21.7 ms: 1.03x faster                                                       |
| telco                   | 6.43 ms                                                | 6.26 ms: 1.03x faster                                                       |
| pathlib                 | 18.1 ms                                                | 17.6 ms: 1.03x faster                                                       |
| scimark_sparse_mat_mult | 4.59 ms                                                | 4.47 ms: 1.03x faster                                                       |
| thrift                  | 760 us                                                 | 742 us: 1.02x faster                                                        |
| scimark_monte_carlo     | 68.0 ms                                                | 66.4 ms: 1.02x faster                                                       |
| async_generators        | 356 ms                                                 | 348 ms: 1.02x faster                                                        |
| spectral_norm           | 98.1 ms                                                | 96.0 ms: 1.02x faster                                                       |
| xml_etree_parse         | 160 ms                                                 | 157 ms: 1.02x faster                                                        |
| mako                    | 9.83 ms                                                | 9.63 ms: 1.02x faster                                                       |
| sympy_sum               | 166 ms                                                 | 162 ms: 1.02x faster                                                        |
| pickle_list             | 4.14 us                                                | 4.06 us: 1.02x faster                                                       |
| django_template         | 32.3 ms                                                | 32.0 ms: 1.01x faster                                                       |
| gc_traversal            | 3.82 ms                                                | 3.81 ms: 1.00x faster                                                       |
| xml_etree_process       | 53.7 ms                                                | 54.1 ms: 1.01x slower                                                       |
| unpack_sequence         | 44.5 ns                                                | 44.9 ns: 1.01x slower                                                       |
| python_startup          | 8.58 ms                                                | 8.68 ms: 1.01x slower                                                       |
| async_tree_io           | 1.30 sec                                               | 1.32 sec: 1.01x slower                                                      |
| regex_effbot            | 3.46 ms                                                | 3.51 ms: 1.02x slower                                                       |
| async_tree_cpu_io_mixed | 736 ms                                                 | 751 ms: 1.02x slower                                                        |
| sqlglot_transpile       | 1.65 ms                                                | 1.68 ms: 1.02x slower                                                       |
| pickle                  | 9.90 us                                                | 10.2 us: 1.03x slower                                                       |
| sqlglot_parse           | 1.36 ms                                                | 1.40 ms: 1.03x slower                                                       |
| python_startup_no_site  | 6.04 ms                                                | 6.22 ms: 1.03x slower                                                       |
| generators              | 73.5 ms                                                | 75.9 ms: 1.03x slower                                                       |
| regex_dna               | 203 ms                                                 | 211 ms: 1.04x slower                                                        |
| xml_etree_generate      | 75.9 ms                                                | 78.8 ms: 1.04x slower                                                       |
| sqlite_synth            | 2.48 us                                                | 2.58 us: 1.04x slower                                                       |
| async_tree_memoization  | 624 ms                                                 | 655 ms: 1.05x slower                                                        |
| xml_etree_iterparse     | 104 ms                                                 | 109 ms: 1.05x slower                                                        |
| nbody                   | 90.0 ms                                                | 94.8 ms: 1.05x slower                                                       |
| dask                    | 365 ms                                                 | 492 ms: 1.35x slower                                                        |
| Geometric mean          | (ref)                                                  | 1.04x faster                                                                |

Benchmark hidden because not significant (8): async_tree_none, meteor_contest, chameleon, unpickle, djangocms, bench_mp_pool, unpickle_list, scimark_lu
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230115-3.12.0a4+-697dc1e/bm-20230115-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-697dc1e.json: mypy
