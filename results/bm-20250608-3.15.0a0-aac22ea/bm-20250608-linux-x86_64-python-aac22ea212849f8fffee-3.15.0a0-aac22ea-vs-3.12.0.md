# Results vs. 3.12.0

- fork: python
- ref: aac22ea212849f8fffee
- machine: linux-x86_64
- commit hash: aac22ea
- commit date: 2025-06-08
- overall geometric mean: 1.085x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250608-linux-x86_64-python-aac22ea212849f8fffee-3.15.0a0-aac22ea |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 256 ms: 1.07x faster                                                  |
| docutils       | 2.77 sec                                               | 2.59 sec: 1.07x faster                                                |
| Geometric mean | (ref)                                                  | 1.07x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250608-linux-x86_64-python-aac22ea212849f8fffee-3.15.0a0-aac22ea |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 616 ms: 1.92x faster                                                  |
| async_tree_io              | 1.16 sec                                               | 603 ms: 1.92x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 317 ms: 1.82x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 318 ms: 1.81x faster                                                  |
| async_tree_none            | 472 ms                                                 | 264 ms: 1.79x faster                                                  |
| async_tree_none_tg         | 450 ms                                                 | 252 ms: 1.78x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 499 ms: 1.45x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 508 ms: 1.43x faster                                                  |
| Geometric mean             | (ref)                                                  | 1.73x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250608-linux-x86_64-python-aac22ea212849f8fffee-3.15.0a0-aac22ea |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 71.5 ms: 1.18x faster                                                 |
| pidigits       | 187 ms                                                 | 192 ms: 1.03x slower                                                  |
| nbody          | 97.0 ms                                                | 102 ms: 1.05x slower                                                  |
| Geometric mean | (ref)                                                  | 1.03x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250608-linux-x86_64-python-aac22ea212849f8fffee-3.15.0a0-aac22ea |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 127 ms: 1.17x faster                                                  |
| regex_effbot   | 3.61 ms                                                | 3.25 ms: 1.11x faster                                                 |
| regex_dna      | 212 ms                                                 | 210 ms: 1.01x faster                                                  |
| regex_v8       | 23.1 ms                                                | 23.3 ms: 1.01x slower                                                 |
| Geometric mean | (ref)                                                  | 1.07x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250608-linux-x86_64-python-aac22ea212849f8fffee-3.15.0a0-aac22ea |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.06 sec: 1.13x faster                                                |
| xml_etree_parse      | 159 ms                                                 | 144 ms: 1.11x faster                                                  |
| xml_etree_iterparse  | 107 ms                                                 | 99.7 ms: 1.07x faster                                                 |
| unpickle_pure_python | 230 us                                                 | 219 us: 1.05x faster                                                  |
| xml_etree_generate   | 89.2 ms                                                | 85.9 ms: 1.04x faster                                                 |
| xml_etree_process    | 61.7 ms                                                | 61.0 ms: 1.01x faster                                                 |
| pickle_pure_python   | 324 us                                                 | 321 us: 1.01x faster                                                  |
| json_dumps           | 10.4 ms                                                | 11.1 ms: 1.07x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                          |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250608-linux-x86_64-python-aac22ea212849f8fffee-3.15.0a0-aac22ea |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 6.90 ms: 1.00x faster                                                 |
| python_startup         | 9.55 ms                                                | 12.2 ms: 1.27x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.13x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250608-linux-x86_64-python-aac22ea212849f8fffee-3.15.0a0-aac22ea |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 32.3 ms: 1.07x faster                                                 |
| mako            | 11.9 ms                                                | 11.3 ms: 1.05x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.06x faster                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250608-linux-x86_64-python-aac22ea212849f8fffee-3.15.0a0-aac22ea |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mdp                        | 2.63 sec                                               | 1.22 sec: 2.15x faster                                                |
| async_tree_io_tg           | 1.18 sec                                               | 616 ms: 1.92x faster                                                  |
| async_tree_io              | 1.16 sec                                               | 603 ms: 1.92x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 317 ms: 1.82x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 318 ms: 1.81x faster                                                  |
| async_tree_none            | 472 ms                                                 | 264 ms: 1.79x faster                                                  |
| async_tree_none_tg         | 450 ms                                                 | 252 ms: 1.78x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 499 ms: 1.45x faster                                                  |
| deepcopy                   | 371 us                                                 | 256 us: 1.45x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 508 ms: 1.43x faster                                                  |
| deepcopy_memo              | 40.7 us                                                | 29.2 us: 1.40x faster                                                 |
| comprehensions             | 21.8 us                                                | 16.3 us: 1.34x faster                                                 |
| go                         | 139 ms                                                 | 111 ms: 1.26x faster                                                  |
| deepcopy_reduce            | 3.35 us                                                | 2.71 us: 1.23x faster                                                 |
| float                      | 84.7 ms                                                | 71.5 ms: 1.18x faster                                                 |
| regex_compile              | 148 ms                                                 | 127 ms: 1.17x faster                                                  |
| raytrace                   | 312 ms                                                 | 270 ms: 1.15x faster                                                  |
| dulwich_log                | 68.5 ms                                                | 60.1 ms: 1.14x faster                                                 |
| sympy_sum                  | 169 ms                                                 | 149 ms: 1.13x faster                                                  |
| tomli_loads                | 2.33 sec                                               | 2.06 sec: 1.13x faster                                                |
| async_generators           | 463 ms                                                 | 409 ms: 1.13x faster                                                  |
| pyflate                    | 482 ms                                                 | 427 ms: 1.13x faster                                                  |
| sympy_integrate            | 21.4 ms                                                | 19.0 ms: 1.13x faster                                                 |
| scimark_monte_carlo        | 75.1 ms                                                | 67.2 ms: 1.12x faster                                                 |
| sympy_str                  | 300 ms                                                 | 269 ms: 1.12x faster                                                  |
| regex_effbot               | 3.61 ms                                                | 3.25 ms: 1.11x faster                                                 |
| xml_etree_parse            | 159 ms                                                 | 144 ms: 1.11x faster                                                  |
| pathlib                    | 19.3 ms                                                | 17.5 ms: 1.11x faster                                                 |
| chaos                      | 67.0 ms                                                | 61.3 ms: 1.09x faster                                                 |
| crypto_pyaes               | 81.9 ms                                                | 75.2 ms: 1.09x faster                                                 |
| django_template            | 34.6 ms                                                | 32.3 ms: 1.07x faster                                                 |
| xml_etree_iterparse        | 107 ms                                                 | 99.7 ms: 1.07x faster                                                 |
| 2to3                       | 274 ms                                                 | 256 ms: 1.07x faster                                                  |
| docutils                   | 2.77 sec                                               | 2.59 sec: 1.07x faster                                                |
| scimark_sor                | 129 ms                                                 | 121 ms: 1.07x faster                                                  |
| richards                   | 45.8 ms                                                | 43.0 ms: 1.07x faster                                                 |
| hexiom                     | 6.41 ms                                                | 6.05 ms: 1.06x faster                                                 |
| meteor_contest             | 112 ms                                                 | 106 ms: 1.06x faster                                                  |
| spectral_norm              | 115 ms                                                 | 109 ms: 1.05x faster                                                  |
| mako                       | 11.9 ms                                                | 11.3 ms: 1.05x faster                                                 |
| unpickle_pure_python       | 230 us                                                 | 219 us: 1.05x faster                                                  |
| generators                 | 31.2 ms                                                | 29.8 ms: 1.05x faster                                                 |
| richards_super             | 51.5 ms                                                | 49.2 ms: 1.05x faster                                                 |
| deltablue                  | 3.72 ms                                                | 3.55 ms: 1.05x faster                                                 |
| sympy_expand               | 478 ms                                                 | 457 ms: 1.05x faster                                                  |
| logging_simple             | 6.46 us                                                | 6.19 us: 1.04x faster                                                 |
| logging_format             | 7.23 us                                                | 6.97 us: 1.04x faster                                                 |
| xml_etree_generate         | 89.2 ms                                                | 85.9 ms: 1.04x faster                                                 |
| nqueens                    | 83.3 ms                                                | 81.7 ms: 1.02x faster                                                 |
| pycparser                  | 1.18 sec                                               | 1.16 sec: 1.01x faster                                                |
| xml_etree_process          | 61.7 ms                                                | 61.0 ms: 1.01x faster                                                 |
| regex_dna                  | 212 ms                                                 | 210 ms: 1.01x faster                                                  |
| pickle_pure_python         | 324 us                                                 | 321 us: 1.01x faster                                                  |
| scimark_fft                | 382 ms                                                 | 379 ms: 1.01x faster                                                  |
| python_startup_no_site     | 6.94 ms                                                | 6.90 ms: 1.00x faster                                                 |
| regex_v8                   | 23.1 ms                                                | 23.3 ms: 1.01x slower                                                 |
| scimark_lu                 | 118 ms                                                 | 119 ms: 1.01x slower                                                  |
| fannkuch                   | 417 ms                                                 | 421 ms: 1.01x slower                                                  |
| sqlite_synth               | 2.83 us                                                | 2.86 us: 1.01x slower                                                 |
| json                       | 5.26 ms                                                | 5.32 ms: 1.01x slower                                                 |
| pprint_safe_repr           | 776 ms                                                 | 786 ms: 1.01x slower                                                  |
| pidigits                   | 187 ms                                                 | 192 ms: 1.03x slower                                                  |
| pprint_pformat             | 1.57 sec                                               | 1.62 sec: 1.03x slower                                                |
| nbody                      | 97.0 ms                                                | 102 ms: 1.05x slower                                                  |
| typing_runtime_protocols   | 158 us                                                 | 167 us: 1.06x slower                                                  |
| json_dumps                 | 10.4 ms                                                | 11.1 ms: 1.07x slower                                                 |
| coroutines                 | 23.2 ms                                                | 25.0 ms: 1.08x slower                                                 |
| telco                      | 7.10 ms                                                | 8.15 ms: 1.15x slower                                                 |
| gc_traversal               | 3.79 ms                                                | 4.75 ms: 1.25x slower                                                 |
| python_startup             | 9.55 ms                                                | 12.2 ms: 1.27x slower                                                 |
| create_gc_cycles           | 1.48 ms                                                | 2.56 ms: 1.73x slower                                                 |
| logging_silent             | 104 ns                                                 | 477 ns: 4.57x slower                                                  |
| coverage                   | 72.7 ms                                                | 439 ms: 6.04x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.06x faster                                                          |

Benchmark hidden because not significant (3): scimark_sparse_mat_mult, json_loads, asyncio_websockets
Ignored benchmarks (22) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250608-3.15.0a0-aac22ea/bm-20250608-linux-x86_64-python-aac22ea212849f8fffee-3.15.0a0-aac22ea.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.085x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.13x