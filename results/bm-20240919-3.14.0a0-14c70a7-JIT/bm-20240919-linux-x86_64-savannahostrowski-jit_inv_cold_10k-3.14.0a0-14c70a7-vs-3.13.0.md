# Results vs. 3.13.0

- fork: savannahostrowski
- ref: jit_inv_cold_10k
- machine: linux-x86_64
- commit hash: 14c70a7
- commit date: 2024-09-19
- overall geometric mean: 1.013x faster
- HPT reliability: 65.10%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.95x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240919-linux-x86_64-savannahostrowski-jit_inv_cold_10k-3.14.0a0-14c70a7 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 285 ms: 1.07x slower                                                         |
| docutils       | 2.59 sec                                               | 2.88 sec: 1.11x slower                                                       |
| html5lib       | 64.2 ms                                                | 63.9 ms: 1.00x faster                                                        |
| tornado_http   | 92.4 ms                                                | 95.5 ms: 1.03x slower                                                        |
| Geometric mean | (ref)                                                  | 1.05x slower                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240919-linux-x86_64-savannahostrowski-jit_inv_cold_10k-3.14.0a0-14c70a7 |
|---------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg | 464 ms                                                 | 387 ms: 1.20x faster                                                         |
| async_tree_memoization    | 442 ms                                                 | 395 ms: 1.12x faster                                                         |
| async_tree_none           | 351 ms                                                 | 321 ms: 1.09x faster                                                         |
| async_tree_none_tg        | 321 ms                                                 | 299 ms: 1.07x faster                                                         |
| async_tree_cpu_io_mixed   | 577 ms                                                 | 558 ms: 1.03x faster                                                         |
| asyncio_websockets        | 552 ms                                                 | 556 ms: 1.01x slower                                                         |
| async_tree_io_tg          | 857 ms                                                 | 874 ms: 1.02x slower                                                         |
| coroutines                | 22.7 ms                                                | 23.4 ms: 1.03x slower                                                        |
| async_tree_io             | 842 ms                                                 | 883 ms: 1.05x slower                                                         |
| async_generators          | 436 ms                                                 | 460 ms: 1.05x slower                                                         |
| Geometric mean            | (ref)                                                  | 1.03x faster                                                                 |

Benchmark hidden because not significant (1): async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240919-linux-x86_64-savannahostrowski-jit_inv_cold_10k-3.14.0a0-14c70a7 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 79.2 ms                                                | 71.5 ms: 1.11x faster                                                        |
| nbody          | 87.0 ms                                                | 79.7 ms: 1.09x faster                                                        |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                                         |
| Geometric mean | (ref)                                                  | 1.07x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240919-linux-x86_64-savannahostrowski-jit_inv_cold_10k-3.14.0a0-14c70a7 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                | 25.5 ms: 1.03x faster                                                        |
| regex_effbot   | 3.73 ms                                                | 3.65 ms: 1.02x faster                                                        |
| regex_dna      | 218 ms                                                 | 215 ms: 1.01x faster                                                         |
| regex_compile  | 132 ms                                                 | 139 ms: 1.05x slower                                                         |
| Geometric mean | (ref)                                                  | 1.00x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240919-linux-x86_64-savannahostrowski-jit_inv_cold_10k-3.14.0a0-14c70a7 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_process    | 60.6 ms                                                | 55.5 ms: 1.09x faster                                                        |
| tomli_loads          | 2.14 sec                                               | 1.96 sec: 1.09x faster                                                       |
| xml_etree_generate   | 86.7 ms                                                | 79.8 ms: 1.09x faster                                                        |
| xml_etree_parse      | 156 ms                                                 | 145 ms: 1.07x faster                                                         |
| json_dumps           | 10.6 ms                                                | 10.1 ms: 1.05x faster                                                        |
| xml_etree_iterparse  | 101 ms                                                 | 99.4 ms: 1.02x faster                                                        |
| json_loads           | 27.2 us                                                | 26.8 us: 1.02x faster                                                        |
| pickle_pure_python   | 310 us                                                 | 306 us: 1.01x faster                                                         |
| unpickle_pure_python | 216 us                                                 | 219 us: 1.01x slower                                                         |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240919-linux-x86_64-savannahostrowski-jit_inv_cold_10k-3.14.0a0-14c70a7 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 12.5 ms                                                | 10.5 ms: 1.19x faster                                                        |
| python_startup_no_site | 6.96 ms                                                | 7.04 ms: 1.01x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240919-linux-x86_64-savannahostrowski-jit_inv_cold_10k-3.14.0a0-14c70a7 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 10.0 ms: 1.10x faster                                                        |
| django_template | 35.2 ms                                                | 35.4 ms: 1.01x slower                                                        |
| genshi_text     | 23.5 ms                                                | 25.5 ms: 1.08x slower                                                        |
| genshi_xml      | 50.9 ms                                                | 61.0 ms: 1.20x slower                                                        |
| Geometric mean  | (ref)                                                  | 1.04x slower                                                                 |

All benchmarks:
===============

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240919-linux-x86_64-savannahostrowski-jit_inv_cold_10k-3.14.0a0-14c70a7 |
|---------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| deepcopy_memo             | 39.1 us                                                | 27.1 us: 1.44x faster                                                        |
| create_gc_cycles          | 2.41 ms                                                | 1.72 ms: 1.40x faster                                                        |
| deepcopy                  | 358 us                                                 | 265 us: 1.35x faster                                                         |
| deepcopy_reduce           | 3.20 us                                                | 2.63 us: 1.22x faster                                                        |
| async_tree_memoization_tg | 464 ms                                                 | 387 ms: 1.20x faster                                                         |
| python_startup            | 12.5 ms                                                | 10.5 ms: 1.19x faster                                                        |
| gc_traversal              | 4.37 ms                                                | 3.71 ms: 1.18x faster                                                        |
| scimark_fft               | 364 ms                                                 | 309 ms: 1.18x faster                                                         |
| richards_super            | 54.9 ms                                                | 47.0 ms: 1.17x faster                                                        |
| richards                  | 48.7 ms                                                | 43.5 ms: 1.12x faster                                                        |
| async_tree_memoization    | 442 ms                                                 | 395 ms: 1.12x faster                                                         |
| float                     | 79.2 ms                                                | 71.5 ms: 1.11x faster                                                        |
| scimark_sparse_mat_mult   | 5.04 ms                                                | 4.56 ms: 1.11x faster                                                        |
| mako                      | 11.1 ms                                                | 10.0 ms: 1.10x faster                                                        |
| crypto_pyaes              | 75.3 ms                                                | 68.2 ms: 1.10x faster                                                        |
| xml_etree_process         | 60.6 ms                                                | 55.5 ms: 1.09x faster                                                        |
| async_tree_none           | 351 ms                                                 | 321 ms: 1.09x faster                                                         |
| nbody                     | 87.0 ms                                                | 79.7 ms: 1.09x faster                                                        |
| tomli_loads               | 2.14 sec                                               | 1.96 sec: 1.09x faster                                                       |
| scimark_monte_carlo       | 67.4 ms                                                | 61.9 ms: 1.09x faster                                                        |
| xml_etree_generate        | 86.7 ms                                                | 79.8 ms: 1.09x faster                                                        |
| pathlib                   | 17.5 ms                                                | 16.2 ms: 1.08x faster                                                        |
| xml_etree_parse           | 156 ms                                                 | 145 ms: 1.07x faster                                                         |
| async_tree_none_tg        | 321 ms                                                 | 299 ms: 1.07x faster                                                         |
| json                      | 5.36 ms                                                | 5.02 ms: 1.07x faster                                                        |
| scimark_sor               | 124 ms                                                 | 117 ms: 1.06x faster                                                         |
| telco                     | 8.54 ms                                                | 8.10 ms: 1.05x faster                                                        |
| go                        | 144 ms                                                 | 137 ms: 1.05x faster                                                         |
| fannkuch                  | 404 ms                                                 | 386 ms: 1.05x faster                                                         |
| json_dumps                | 10.6 ms                                                | 10.1 ms: 1.05x faster                                                        |
| mdp                       | 2.72 sec                                               | 2.62 sec: 1.04x faster                                                       |
| async_tree_cpu_io_mixed   | 577 ms                                                 | 558 ms: 1.03x faster                                                         |
| pyflate                   | 471 ms                                                 | 456 ms: 1.03x faster                                                         |
| regex_v8                  | 26.2 ms                                                | 25.5 ms: 1.03x faster                                                        |
| thrift                    | 809 us                                                 | 790 us: 1.02x faster                                                         |
| regex_effbot              | 3.73 ms                                                | 3.65 ms: 1.02x faster                                                        |
| spectral_norm             | 115 ms                                                 | 113 ms: 1.02x faster                                                         |
| logging_format            | 6.40 us                                                | 6.28 us: 1.02x faster                                                        |
| xml_etree_iterparse       | 101 ms                                                 | 99.4 ms: 1.02x faster                                                        |
| json_loads                | 27.2 us                                                | 26.8 us: 1.02x faster                                                        |
| regex_dna                 | 218 ms                                                 | 215 ms: 1.01x faster                                                         |
| pickle_pure_python        | 310 us                                                 | 306 us: 1.01x faster                                                         |
| meteor_contest            | 109 ms                                                 | 107 ms: 1.01x faster                                                         |
| pycparser                 | 1.20 sec                                               | 1.19 sec: 1.01x faster                                                       |
| logging_simple            | 5.72 us                                                | 5.67 us: 1.01x faster                                                        |
| html5lib                  | 64.2 ms                                                | 63.9 ms: 1.00x faster                                                        |
| pidigits                  | 186 ms                                                 | 186 ms: 1.00x faster                                                         |
| django_template           | 35.2 ms                                                | 35.4 ms: 1.01x slower                                                        |
| asyncio_websockets        | 552 ms                                                 | 556 ms: 1.01x slower                                                         |
| python_startup_no_site    | 6.96 ms                                                | 7.04 ms: 1.01x slower                                                        |
| logging_silent            | 102 ns                                                 | 103 ns: 1.01x slower                                                         |
| unpickle_pure_python      | 216 us                                                 | 219 us: 1.01x slower                                                         |
| coverage                  | 84.0 ms                                                | 85.3 ms: 1.02x slower                                                        |
| comprehensions            | 16.5 us                                                | 16.8 us: 1.02x slower                                                        |
| pprint_safe_repr          | 728 ms                                                 | 742 ms: 1.02x slower                                                         |
| async_tree_io_tg          | 857 ms                                                 | 874 ms: 1.02x slower                                                         |
| scimark_lu                | 113 ms                                                 | 115 ms: 1.02x slower                                                         |
| bench_thread_pool         | 822 us                                                 | 841 us: 1.02x slower                                                         |
| chaos                     | 58.1 ms                                                | 59.6 ms: 1.03x slower                                                        |
| bpe_tokeniser             | 4.75 sec                                               | 4.88 sec: 1.03x slower                                                       |
| coroutines                | 22.7 ms                                                | 23.4 ms: 1.03x slower                                                        |
| tornado_http              | 92.4 ms                                                | 95.5 ms: 1.03x slower                                                        |
| pprint_pformat            | 1.49 sec                                               | 1.55 sec: 1.04x slower                                                       |
| async_tree_io             | 842 ms                                                 | 883 ms: 1.05x slower                                                         |
| regex_compile             | 132 ms                                                 | 139 ms: 1.05x slower                                                         |
| raytrace                  | 267 ms                                                 | 281 ms: 1.05x slower                                                         |
| sqlglot_parse             | 1.27 ms                                                | 1.34 ms: 1.05x slower                                                        |
| async_generators          | 436 ms                                                 | 460 ms: 1.05x slower                                                         |
| 2to3                      | 267 ms                                                 | 285 ms: 1.07x slower                                                         |
| sqlglot_transpile         | 1.58 ms                                                | 1.69 ms: 1.07x slower                                                        |
| dulwich_log               | 64.3 ms                                                | 68.9 ms: 1.07x slower                                                        |
| sqlglot_normalize         | 108 ms                                                 | 116 ms: 1.08x slower                                                         |
| genshi_text               | 23.5 ms                                                | 25.5 ms: 1.08x slower                                                        |
| sympy_expand              | 463 ms                                                 | 505 ms: 1.09x slower                                                         |
| docutils                  | 2.59 sec                                               | 2.88 sec: 1.11x slower                                                       |
| sympy_str                 | 275 ms                                                 | 306 ms: 1.11x slower                                                         |
| nqueens                   | 78.4 ms                                                | 88.1 ms: 1.12x slower                                                        |
| deltablue                 | 3.23 ms                                                | 3.68 ms: 1.14x slower                                                        |
| sympy_sum                 | 150 ms                                                 | 173 ms: 1.15x slower                                                         |
| sqlglot_optimize          | 53.7 ms                                                | 63.7 ms: 1.18x slower                                                        |
| genshi_xml                | 50.9 ms                                                | 61.0 ms: 1.20x slower                                                        |
| pylint                    | 313 ms                                                 | 382 ms: 1.22x slower                                                         |
| generators                | 29.0 ms                                                | 36.2 ms: 1.25x slower                                                        |
| hexiom                    | 6.16 ms                                                | 7.89 ms: 1.28x slower                                                        |
| sympy_integrate           | 19.9 ms                                                | 26.5 ms: 1.33x slower                                                        |
| Geometric mean            | (ref)                                                  | 1.01x faster                                                                 |

Benchmark hidden because not significant (3): typing_runtime_protocols, async_tree_cpu_io_mixed_tg, bench_mp_pool
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20240919-3.14.0a0-14c70a7-JIT/bm-20240919-linux-x86_64-savannahostrowski-jit_inv_cold_10k-3.14.0a0-14c70a7.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.013x faster
# HPT report

- Reliability score: 65.10% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.95x