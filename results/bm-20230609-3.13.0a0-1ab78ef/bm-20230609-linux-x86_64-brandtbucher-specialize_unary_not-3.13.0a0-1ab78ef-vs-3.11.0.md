
# Results vs. 3.11.0

- fork: brandtbucher
- ref: specialize_unary_not
- machine: linux-x86_64
- commit hash: 1ab78ef
- commit date: 2023-06-09
- overall geometric mean: 1.02x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230609-linux-x86_64-brandtbucher-specialize_unary_not-3.13.0a0-1ab78ef |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| docutils       | 2.63 sec                                               | 2.74 sec: 1.04x slower                                                      |
| tornado_http   | 96.3 ms                                                | 103 ms: 1.07x slower                                                        |
| Geometric mean | (ref)                                                  | 1.05x slower                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230609-linux-x86_64-brandtbucher-specialize_unary_not-3.13.0a0-1ab78ef |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 93.1 ms                                                | 89.7 ms: 1.04x faster                                                       |
| pidigits       | 198 ms                                                 | 197 ms: 1.00x faster                                                        |
| float          | 77.2 ms                                                | 81.5 ms: 1.06x slower                                                       |
| Geometric mean | (ref)                                                  | 1.00x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230609-linux-x86_64-brandtbucher-specialize_unary_not-3.13.0a0-1ab78ef |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.53 ms: 1.13x faster                                                       |
| regex_v8       | 22.0 ms                                                | 21.7 ms: 1.01x faster                                                       |
| regex_dna      | 204 ms                                                 | 207 ms: 1.02x slower                                                        |
| regex_compile  | 138 ms                                                 | 146 ms: 1.06x slower                                                        |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230609-linux-x86_64-brandtbucher-specialize_unary_not-3.13.0a0-1ab78ef |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.84 ms: 1.28x faster                                                       |
| json_loads           | 26.5 us                                                | 25.0 us: 1.06x faster                                                       |
| xml_etree_parse      | 158 ms                                                 | 153 ms: 1.03x faster                                                        |
| unpickle_pure_python | 228 us                                                 | 226 us: 1.01x faster                                                        |
| unpickle_list        | 4.91 us                                                | 4.87 us: 1.01x faster                                                       |
| tomli_loads          | 2.22 sec                                               | 2.27 sec: 1.02x slower                                                      |
| pickle_dict          | 31.1 us                                                | 32.1 us: 1.03x slower                                                       |
| pickle_pure_python   | 306 us                                                 | 317 us: 1.04x slower                                                        |
| pickle               | 10.1 us                                                | 10.6 us: 1.05x slower                                                       |
| xml_etree_process    | 53.9 ms                                                | 58.5 ms: 1.09x slower                                                       |
| unpickle             | 13.7 us                                                | 15.0 us: 1.10x slower                                                       |
| xml_etree_generate   | 76.2 ms                                                | 84.9 ms: 1.11x slower                                                       |
| pickle_list          | 4.11 us                                                | 4.75 us: 1.15x slower                                                       |
| Geometric mean       | (ref)                                                  | 1.02x slower                                                                |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230609-linux-x86_64-brandtbucher-specialize_unary_not-3.13.0a0-1ab78ef |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 9.28 ms: 1.09x slower                                                       |
| python_startup_no_site | 6.01 ms                                                | 6.76 ms: 1.12x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.11x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230609-linux-x86_64-brandtbucher-specialize_unary_not-3.13.0a0-1ab78ef |
|-----------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako      | 10.1 ms                                                | 10.6 ms: 1.05x slower                                                       |

All benchmarks:
===============

| Benchmark                | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230609-linux-x86_64-brandtbucher-specialize_unary_not-3.13.0a0-1ab78ef |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 486 us                                                 | 143 us: 3.39x faster                                                        |
| generators               | 73.5 ms                                                | 30.8 ms: 2.39x faster                                                       |
| asyncio_tcp              | 922 ms                                                 | 518 ms: 1.78x faster                                                        |
| asyncio_tcp_ssl          | 3.14 sec                                               | 1.80 sec: 1.74x faster                                                      |
| json_dumps               | 12.6 ms                                                | 9.84 ms: 1.28x faster                                                       |
| mypy2                    | 420 ms                                                 | 345 ms: 1.22x faster                                                        |
| regex_effbot             | 3.99 ms                                                | 3.53 ms: 1.13x faster                                                       |
| coroutines               | 25.5 ms                                                | 22.8 ms: 1.12x faster                                                       |
| richards_super           | 56.8 ms                                                | 51.4 ms: 1.10x faster                                                       |
| comprehensions           | 22.4 us                                                | 20.8 us: 1.08x faster                                                       |
| chaos                    | 69.2 ms                                                | 64.9 ms: 1.07x faster                                                       |
| async_tree_none          | 526 ms                                                 | 496 ms: 1.06x faster                                                        |
| json_loads               | 26.5 us                                                | 25.0 us: 1.06x faster                                                       |
| async_tree_io            | 1.30 sec                                               | 1.23 sec: 1.06x faster                                                      |
| coverage                 | 100 ms                                                 | 95.0 ms: 1.05x faster                                                       |
| async_tree_memoization   | 627 ms                                                 | 600 ms: 1.05x faster                                                        |
| nbody                    | 93.1 ms                                                | 89.7 ms: 1.04x faster                                                       |
| json                     | 4.94 ms                                                | 4.78 ms: 1.03x faster                                                       |
| xml_etree_parse          | 158 ms                                                 | 153 ms: 1.03x faster                                                        |
| mdp                      | 2.62 sec                                               | 2.54 sec: 1.03x faster                                                      |
| nqueens                  | 83.4 ms                                                | 81.3 ms: 1.03x faster                                                       |
| sqlglot_parse            | 1.40 ms                                                | 1.38 ms: 1.02x faster                                                       |
| regex_v8                 | 22.0 ms                                                | 21.7 ms: 1.01x faster                                                       |
| deltablue                | 3.67 ms                                                | 3.63 ms: 1.01x faster                                                       |
| unpickle_pure_python     | 228 us                                                 | 226 us: 1.01x faster                                                        |
| go                       | 140 ms                                                 | 138 ms: 1.01x faster                                                        |
| unpickle_list            | 4.91 us                                                | 4.87 us: 1.01x faster                                                       |
| hexiom                   | 6.37 ms                                                | 6.34 ms: 1.01x faster                                                       |
| pidigits                 | 198 ms                                                 | 197 ms: 1.00x faster                                                        |
| create_gc_cycles         | 1.49 ms                                                | 1.50 ms: 1.01x slower                                                       |
| sqlglot_transpile        | 1.70 ms                                                | 1.71 ms: 1.01x slower                                                       |
| gc_traversal             | 4.02 ms                                                | 4.07 ms: 1.01x slower                                                       |
| raytrace                 | 297 ms                                                 | 301 ms: 1.01x slower                                                        |
| regex_dna                | 204 ms                                                 | 207 ms: 1.02x slower                                                        |
| pathlib                  | 18.2 ms                                                | 18.5 ms: 1.02x slower                                                       |
| pycparser                | 1.18 sec                                               | 1.20 sec: 1.02x slower                                                      |
| bench_thread_pool        | 819 us                                                 | 836 us: 1.02x slower                                                        |
| tomli_loads              | 2.22 sec                                               | 2.27 sec: 1.02x slower                                                      |
| pickle_dict              | 31.1 us                                                | 32.1 us: 1.03x slower                                                       |
| pickle_pure_python       | 306 us                                                 | 317 us: 1.04x slower                                                        |
| sqlglot_normalize        | 108 ms                                                 | 112 ms: 1.04x slower                                                        |
| pprint_pformat           | 1.46 sec                                               | 1.51 sec: 1.04x slower                                                      |
| sqlglot_optimize         | 53.1 ms                                                | 55.3 ms: 1.04x slower                                                       |
| docutils                 | 2.63 sec                                               | 2.74 sec: 1.04x slower                                                      |
| scimark_lu               | 110 ms                                                 | 115 ms: 1.04x slower                                                        |
| telco                    | 6.58 ms                                                | 6.89 ms: 1.05x slower                                                       |
| mako                     | 10.1 ms                                                | 10.6 ms: 1.05x slower                                                       |
| deepcopy                 | 342 us                                                 | 359 us: 1.05x slower                                                        |
| scimark_sparse_mat_mult  | 4.50 ms                                                | 4.73 ms: 1.05x slower                                                       |
| deepcopy_memo            | 37.0 us                                                | 39.0 us: 1.05x slower                                                       |
| pickle                   | 10.1 us                                                | 10.6 us: 1.05x slower                                                       |
| float                    | 77.2 ms                                                | 81.5 ms: 1.06x slower                                                       |
| regex_compile            | 138 ms                                                 | 146 ms: 1.06x slower                                                        |
| pprint_safe_repr         | 701 ms                                                 | 744 ms: 1.06x slower                                                        |
| scimark_sor              | 118 ms                                                 | 126 ms: 1.07x slower                                                        |
| tornado_http             | 96.3 ms                                                | 103 ms: 1.07x slower                                                        |
| spectral_norm            | 100 ms                                                 | 107 ms: 1.07x slower                                                        |
| crypto_pyaes             | 74.7 ms                                                | 79.7 ms: 1.07x slower                                                       |
| logging_silent           | 101 ns                                                 | 108 ns: 1.07x slower                                                        |
| dulwich_log              | 63.7 ms                                                | 68.3 ms: 1.07x slower                                                       |
| sqlite_synth             | 2.52 us                                                | 2.71 us: 1.08x slower                                                       |
| logging_format           | 6.68 us                                                | 7.20 us: 1.08x slower                                                       |
| scimark_fft              | 328 ms                                                 | 354 ms: 1.08x slower                                                        |
| pyflate                  | 418 ms                                                 | 454 ms: 1.08x slower                                                        |
| xml_etree_process        | 53.9 ms                                                | 58.5 ms: 1.09x slower                                                       |
| logging_simple           | 6.03 us                                                | 6.56 us: 1.09x slower                                                       |
| python_startup           | 8.52 ms                                                | 9.28 ms: 1.09x slower                                                       |
| scimark_monte_carlo      | 68.1 ms                                                | 74.5 ms: 1.09x slower                                                       |
| deepcopy_reduce          | 2.94 us                                                | 3.22 us: 1.09x slower                                                       |
| unpickle                 | 13.7 us                                                | 15.0 us: 1.10x slower                                                       |
| xml_etree_generate       | 76.2 ms                                                | 84.9 ms: 1.11x slower                                                       |
| python_startup_no_site   | 6.01 ms                                                | 6.76 ms: 1.12x slower                                                       |
| unpack_sequence          | 43.1 ns                                                | 49.0 ns: 1.14x slower                                                       |
| pickle_list              | 4.11 us                                                | 4.75 us: 1.15x slower                                                       |
| async_generators         | 368 ms                                                 | 448 ms: 1.21x slower                                                        |
| dask                     | 360 ms                                                 | 542 ms: 1.51x slower                                                        |
| Geometric mean           | (ref)                                                  | 1.02x faster                                                                |

Benchmark hidden because not significant (6): meteor_contest, async_tree_cpu_io_mixed, bench_mp_pool, richards, fannkuch, xml_etree_iterparse
Ignored benchmarks (18) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
