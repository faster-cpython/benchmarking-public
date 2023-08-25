
# Results vs. 3.11.0

- fork: brandtbucher
- ref: fold_slices
- machine: linux-x86_64
- commit hash: 39619f9
- commit date: 2023-04-06
- overall geometric mean: 1.04x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230406-linux-x86_64-brandtbucher-fold_slices-3.12.0a7+-39619f9 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 250 ms: 1.04x faster                                                |
| docutils       | 2.63 sec                                               | 2.54 sec: 1.03x faster                                              |
| html5lib       | 64.5 ms                                                | 61.2 ms: 1.05x faster                                               |
| tornado_http   | 96.3 ms                                                | 90.9 ms: 1.06x faster                                               |
| Geometric mean | (ref)                                                  | 1.04x faster                                                        |

Benchmark hidden because not significant (1): chameleon

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230406-linux-x86_64-brandtbucher-fold_slices-3.12.0a7+-39619f9 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| nbody          | 93.1 ms                                                | 86.6 ms: 1.07x faster                                               |
| pidigits       | 198 ms                                                 | 188 ms: 1.05x faster                                                |
| float          | 77.2 ms                                                | 73.6 ms: 1.05x faster                                               |
| Geometric mean | (ref)                                                  | 1.06x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230406-linux-x86_64-brandtbucher-fold_slices-3.12.0a7+-39619f9 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.45 ms: 1.16x faster                                               |
| regex_compile  | 138 ms                                                 | 134 ms: 1.03x faster                                                |
| regex_dna      | 204 ms                                                 | 204 ms: 1.00x slower                                                |
| regex_v8       | 22.0 ms                                                | 22.4 ms: 1.01x slower                                               |
| Geometric mean | (ref)                                                  | 1.04x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230406-linux-x86_64-brandtbucher-fold_slices-3.12.0a7+-39619f9 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.53 ms: 1.32x faster                                               |
| unpickle_pure_python | 228 us                                                 | 202 us: 1.13x faster                                                |
| json_loads           | 26.5 us                                                | 24.1 us: 1.10x faster                                               |
| xml_etree_parse      | 158 ms                                                 | 150 ms: 1.06x faster                                                |
| pickle_pure_python   | 306 us                                                 | 290 us: 1.05x faster                                                |
| xml_etree_iterparse  | 104 ms                                                 | 103 ms: 1.01x faster                                                |
| xml_etree_process    | 53.9 ms                                                | 56.2 ms: 1.04x slower                                               |
| pickle_dict          | 31.1 us                                                | 32.6 us: 1.05x slower                                               |
| pickle_list          | 4.11 us                                                | 4.35 us: 1.06x slower                                               |
| xml_etree_generate   | 76.2 ms                                                | 80.9 ms: 1.06x slower                                               |
| pickle               | 10.1 us                                                | 10.9 us: 1.08x slower                                               |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                        |

Benchmark hidden because not significant (2): unpickle, unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230406-linux-x86_64-brandtbucher-fold_slices-3.12.0a7+-39619f9 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 8.84 ms: 1.04x slower                                               |
| python_startup_no_site | 6.01 ms                                                | 6.53 ms: 1.09x slower                                               |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230406-linux-x86_64-brandtbucher-fold_slices-3.12.0a7+-39619f9 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_xml      | 51.8 ms                                                | 47.6 ms: 1.09x faster                                               |
| genshi_text     | 21.6 ms                                                | 21.0 ms: 1.02x faster                                               |
| django_template | 32.6 ms                                                | 33.4 ms: 1.03x slower                                               |
| Geometric mean  | (ref)                                                  | 1.02x faster                                                        |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230406-linux-x86_64-brandtbucher-fold_slices-3.12.0a7+-39619f9 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| generators              | 73.5 ms                                                | 29.2 ms: 2.52x faster                                               |
| asyncio_tcp             | 922 ms                                                 | 500 ms: 1.84x faster                                                |
| json_dumps              | 12.6 ms                                                | 9.53 ms: 1.32x faster                                               |
| mypy2                   | 420 ms                                                 | 335 ms: 1.26x faster                                                |
| regex_effbot            | 3.99 ms                                                | 3.45 ms: 1.16x faster                                               |
| sqlglot_parse           | 1.40 ms                                                | 1.23 ms: 1.14x faster                                               |
| sqlglot_transpile       | 1.70 ms                                                | 1.50 ms: 1.13x faster                                               |
| unpickle_pure_python    | 228 us                                                 | 202 us: 1.13x faster                                                |
| deltablue               | 3.67 ms                                                | 3.30 ms: 1.11x faster                                               |
| json_loads              | 26.5 us                                                | 24.1 us: 1.10x faster                                               |
| aiohttp                 | 1.10 ms                                                | 1.01 ms: 1.09x faster                                               |
| genshi_xml              | 51.8 ms                                                | 47.6 ms: 1.09x faster                                               |
| gunicorn                | 1.18 ms                                                | 1.09 ms: 1.08x faster                                               |
| deepcopy_memo           | 37.0 us                                                | 34.2 us: 1.08x faster                                               |
| richards                | 45.7 ms                                                | 42.5 ms: 1.08x faster                                               |
| coroutines              | 25.5 ms                                                | 23.7 ms: 1.08x faster                                               |
| nbody                   | 93.1 ms                                                | 86.6 ms: 1.07x faster                                               |
| json                    | 4.94 ms                                                | 4.63 ms: 1.07x faster                                               |
| hexiom                  | 6.37 ms                                                | 5.98 ms: 1.07x faster                                               |
| tornado_http            | 96.3 ms                                                | 90.9 ms: 1.06x faster                                               |
| xml_etree_parse         | 158 ms                                                 | 150 ms: 1.06x faster                                                |
| scimark_fft             | 328 ms                                                 | 311 ms: 1.06x faster                                                |
| html5lib                | 64.5 ms                                                | 61.2 ms: 1.05x faster                                               |
| pickle_pure_python      | 306 us                                                 | 290 us: 1.05x faster                                                |
| pidigits                | 198 ms                                                 | 188 ms: 1.05x faster                                                |
| logging_simple          | 6.03 us                                                | 5.74 us: 1.05x faster                                               |
| logging_format          | 6.68 us                                                | 6.36 us: 1.05x faster                                               |
| scimark_sor             | 118 ms                                                 | 112 ms: 1.05x faster                                                |
| chaos                   | 69.2 ms                                                | 65.9 ms: 1.05x faster                                               |
| deepcopy                | 342 us                                                 | 326 us: 1.05x faster                                                |
| float                   | 77.2 ms                                                | 73.6 ms: 1.05x faster                                               |
| meteor_contest          | 107 ms                                                 | 102 ms: 1.05x faster                                                |
| comprehensions          | 22.4 us                                                | 21.4 us: 1.05x faster                                               |
| scimark_sparse_mat_mult | 4.50 ms                                                | 4.31 ms: 1.04x faster                                               |
| mdp                     | 2.62 sec                                               | 2.51 sec: 1.04x faster                                              |
| raytrace                | 297 ms                                                 | 285 ms: 1.04x faster                                                |
| telco                   | 6.58 ms                                                | 6.32 ms: 1.04x faster                                               |
| sqlglot_optimize        | 53.1 ms                                                | 51.0 ms: 1.04x faster                                               |
| go                      | 140 ms                                                 | 134 ms: 1.04x faster                                                |
| spectral_norm           | 100 ms                                                 | 96.1 ms: 1.04x faster                                               |
| 2to3                    | 259 ms                                                 | 250 ms: 1.04x faster                                                |
| bench_thread_pool       | 819 us                                                 | 791 us: 1.03x faster                                                |
| coverage                | 100 ms                                                 | 96.7 ms: 1.03x faster                                               |
| logging_silent          | 101 ns                                                 | 97.7 ns: 1.03x faster                                               |
| docutils                | 2.63 sec                                               | 2.54 sec: 1.03x faster                                              |
| regex_compile           | 138 ms                                                 | 134 ms: 1.03x faster                                                |
| sqlglot_normalize       | 108 ms                                                 | 105 ms: 1.03x faster                                                |
| nqueens                 | 83.4 ms                                                | 81.0 ms: 1.03x faster                                               |
| genshi_text             | 21.6 ms                                                | 21.0 ms: 1.02x faster                                               |
| sympy_integrate         | 21.0 ms                                                | 20.5 ms: 1.02x faster                                               |
| pprint_pformat          | 1.46 sec                                               | 1.42 sec: 1.02x faster                                              |
| pycparser               | 1.18 sec                                               | 1.16 sec: 1.02x faster                                              |
| async_tree_none         | 526 ms                                                 | 515 ms: 1.02x faster                                                |
| fannkuch                | 388 ms                                                 | 380 ms: 1.02x faster                                                |
| sympy_str               | 290 ms                                                 | 285 ms: 1.02x faster                                                |
| pprint_safe_repr        | 701 ms                                                 | 690 ms: 1.02x faster                                                |
| sympy_expand            | 475 ms                                                 | 467 ms: 1.02x faster                                                |
| crypto_pyaes            | 74.7 ms                                                | 73.5 ms: 1.02x faster                                               |
| sqlalchemy_declarative  | 138 ms                                                 | 136 ms: 1.01x faster                                                |
| async_tree_io           | 1.30 sec                                               | 1.28 sec: 1.01x faster                                              |
| pyflate                 | 418 ms                                                 | 414 ms: 1.01x faster                                                |
| xml_etree_iterparse     | 104 ms                                                 | 103 ms: 1.01x faster                                                |
| dulwich_log             | 63.7 ms                                                | 63.3 ms: 1.01x faster                                               |
| pathlib                 | 18.2 ms                                                | 18.2 ms: 1.00x faster                                               |
| regex_dna               | 204 ms                                                 | 204 ms: 1.00x slower                                                |
| scimark_lu              | 110 ms                                                 | 111 ms: 1.01x slower                                                |
| regex_v8                | 22.0 ms                                                | 22.4 ms: 1.01x slower                                               |
| deepcopy_reduce         | 2.94 us                                                | 2.99 us: 1.02x slower                                               |
| unpack_sequence         | 43.1 ns                                                | 43.9 ns: 1.02x slower                                               |
| create_gc_cycles        | 1.49 ms                                                | 1.51 ms: 1.02x slower                                               |
| gc_traversal            | 4.02 ms                                                | 4.10 ms: 1.02x slower                                               |
| django_template         | 32.6 ms                                                | 33.4 ms: 1.03x slower                                               |
| thrift                  | 756 us                                                 | 780 us: 1.03x slower                                                |
| python_startup          | 8.52 ms                                                | 8.84 ms: 1.04x slower                                               |
| sqlite_synth            | 2.52 us                                                | 2.63 us: 1.04x slower                                               |
| xml_etree_process       | 53.9 ms                                                | 56.2 ms: 1.04x slower                                               |
| pickle_dict             | 31.1 us                                                | 32.6 us: 1.05x slower                                               |
| pickle_list             | 4.11 us                                                | 4.35 us: 1.06x slower                                               |
| xml_etree_generate      | 76.2 ms                                                | 80.9 ms: 1.06x slower                                               |
| pickle                  | 10.1 us                                                | 10.9 us: 1.08x slower                                               |
| python_startup_no_site  | 6.01 ms                                                | 6.53 ms: 1.09x slower                                               |
| async_generators        | 368 ms                                                 | 408 ms: 1.11x slower                                                |
| dask                    | 360 ms                                                 | 507 ms: 1.41x slower                                                |
| Geometric mean          | (ref)                                                  | 1.04x faster                                                        |

Benchmark hidden because not significant (11): unpickle, async_tree_memoization, async_tree_cpu_io_mixed, sympy_sum, djangocms, bench_mp_pool, mako, sqlalchemy_imperative, chameleon, unpickle_list, scimark_monte_carlo
Ignored benchmarks (6) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp_ssl, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x
