# Results vs. 3.13.0

- fork: savannahostrowski
- ref: jit_inv_cold_100
- machine: linux-x86_64
- commit hash: 99262b6
- commit date: 2024-09-19
- overall geometric mean: 1.005x faster
- HPT reliability: 54.44%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.94x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240919-linux-x86_64-savannahostrowski-jit_inv_cold_100-3.14.0a0-99262b6 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 318 ms: 1.19x slower                                                         |
| docutils       | 2.59 sec                                               | 2.70 sec: 1.04x slower                                                       |
| html5lib       | 64.2 ms                                                | 63.2 ms: 1.02x faster                                                        |
| tornado_http   | 92.4 ms                                                | 110 ms: 1.19x slower                                                         |
| Geometric mean | (ref)                                                  | 1.10x slower                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240919-linux-x86_64-savannahostrowski-jit_inv_cold_100-3.14.0a0-99262b6 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 464 ms                                                 | 390 ms: 1.19x faster                                                         |
| async_tree_memoization     | 442 ms                                                 | 403 ms: 1.10x faster                                                         |
| async_tree_none            | 351 ms                                                 | 322 ms: 1.09x faster                                                         |
| async_tree_none_tg         | 321 ms                                                 | 306 ms: 1.05x faster                                                         |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 570 ms: 1.01x faster                                                         |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 554 ms: 1.02x slower                                                         |
| async_tree_io_tg           | 857 ms                                                 | 875 ms: 1.02x slower                                                         |
| coroutines                 | 22.7 ms                                                | 23.3 ms: 1.03x slower                                                        |
| async_generators           | 436 ms                                                 | 454 ms: 1.04x slower                                                         |
| async_tree_io              | 842 ms                                                 | 892 ms: 1.06x slower                                                         |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                                 |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240919-linux-x86_64-savannahostrowski-jit_inv_cold_100-3.14.0a0-99262b6 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 79.2 ms                                                | 71.3 ms: 1.11x faster                                                        |
| nbody          | 87.0 ms                                                | 85.5 ms: 1.02x faster                                                        |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                                         |
| Geometric mean | (ref)                                                  | 1.04x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240919-linux-x86_64-savannahostrowski-jit_inv_cold_100-3.14.0a0-99262b6 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.73 ms                                                | 3.62 ms: 1.03x faster                                                        |
| regex_compile  | 132 ms                                                 | 130 ms: 1.02x faster                                                         |
| regex_dna      | 218 ms                                                 | 215 ms: 1.02x faster                                                         |
| regex_v8       | 26.2 ms                                                | 26.4 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                  | 1.01x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240919-linux-x86_64-savannahostrowski-jit_inv_cold_100-3.14.0a0-99262b6 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_parse      | 156 ms                                                 | 146 ms: 1.07x faster                                                         |
| json_dumps           | 10.6 ms                                                | 10.2 ms: 1.03x faster                                                        |
| xml_etree_process    | 60.6 ms                                                | 59.3 ms: 1.02x faster                                                        |
| xml_etree_iterparse  | 101 ms                                                 | 99.7 ms: 1.02x faster                                                        |
| json_loads           | 27.2 us                                                | 26.8 us: 1.01x faster                                                        |
| xml_etree_generate   | 86.7 ms                                                | 85.6 ms: 1.01x faster                                                        |
| tomli_loads          | 2.14 sec                                               | 2.11 sec: 1.01x faster                                                       |
| unpickle_pure_python | 216 us                                                 | 220 us: 1.02x slower                                                         |
| pickle_pure_python   | 310 us                                                 | 331 us: 1.07x slower                                                         |
| Geometric mean       | (ref)                                                  | 1.01x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240919-linux-x86_64-savannahostrowski-jit_inv_cold_100-3.14.0a0-99262b6 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 12.5 ms                                                | 10.5 ms: 1.19x faster                                                        |
| python_startup_no_site | 6.96 ms                                                | 7.05 ms: 1.01x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240919-linux-x86_64-savannahostrowski-jit_inv_cold_100-3.14.0a0-99262b6 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 10.1 ms: 1.10x faster                                                        |
| genshi_text     | 23.5 ms                                                | 24.3 ms: 1.03x slower                                                        |
| django_template | 35.2 ms                                                | 38.4 ms: 1.09x slower                                                        |
| genshi_xml      | 50.9 ms                                                | 57.8 ms: 1.14x slower                                                        |
| Geometric mean  | (ref)                                                  | 1.04x slower                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240919-linux-x86_64-savannahostrowski-jit_inv_cold_100-3.14.0a0-99262b6 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| deepcopy_memo              | 39.1 us                                                | 27.5 us: 1.42x faster                                                        |
| create_gc_cycles           | 2.41 ms                                                | 1.74 ms: 1.39x faster                                                        |
| deepcopy                   | 358 us                                                 | 270 us: 1.33x faster                                                         |
| deepcopy_reduce            | 3.20 us                                                | 2.64 us: 1.21x faster                                                        |
| async_tree_memoization_tg  | 464 ms                                                 | 390 ms: 1.19x faster                                                         |
| python_startup             | 12.5 ms                                                | 10.5 ms: 1.19x faster                                                        |
| go                         | 144 ms                                                 | 122 ms: 1.18x faster                                                         |
| scimark_sparse_mat_mult    | 5.04 ms                                                | 4.47 ms: 1.13x faster                                                        |
| crypto_pyaes               | 75.3 ms                                                | 67.5 ms: 1.12x faster                                                        |
| float                      | 79.2 ms                                                | 71.3 ms: 1.11x faster                                                        |
| gc_traversal               | 4.37 ms                                                | 3.96 ms: 1.10x faster                                                        |
| async_tree_memoization     | 442 ms                                                 | 403 ms: 1.10x faster                                                         |
| mako                       | 11.1 ms                                                | 10.1 ms: 1.10x faster                                                        |
| async_tree_none            | 351 ms                                                 | 322 ms: 1.09x faster                                                         |
| json                       | 5.36 ms                                                | 4.94 ms: 1.09x faster                                                        |
| pathlib                    | 17.5 ms                                                | 16.3 ms: 1.07x faster                                                        |
| xml_etree_parse            | 156 ms                                                 | 146 ms: 1.07x faster                                                         |
| telco                      | 8.54 ms                                                | 8.08 ms: 1.06x faster                                                        |
| spectral_norm              | 115 ms                                                 | 110 ms: 1.05x faster                                                         |
| scimark_sor                | 124 ms                                                 | 118 ms: 1.05x faster                                                         |
| async_tree_none_tg         | 321 ms                                                 | 306 ms: 1.05x faster                                                         |
| fannkuch                   | 404 ms                                                 | 389 ms: 1.04x faster                                                         |
| json_dumps                 | 10.6 ms                                                | 10.2 ms: 1.03x faster                                                        |
| richards_super             | 54.9 ms                                                | 53.2 ms: 1.03x faster                                                        |
| regex_effbot               | 3.73 ms                                                | 3.62 ms: 1.03x faster                                                        |
| thrift                     | 809 us                                                 | 788 us: 1.03x faster                                                         |
| scimark_monte_carlo        | 67.4 ms                                                | 65.9 ms: 1.02x faster                                                        |
| logging_format             | 6.40 us                                                | 6.25 us: 1.02x faster                                                        |
| xml_etree_process          | 60.6 ms                                                | 59.3 ms: 1.02x faster                                                        |
| pycparser                  | 1.20 sec                                               | 1.18 sec: 1.02x faster                                                       |
| regex_compile              | 132 ms                                                 | 130 ms: 1.02x faster                                                         |
| nbody                      | 87.0 ms                                                | 85.5 ms: 1.02x faster                                                        |
| regex_dna                  | 218 ms                                                 | 215 ms: 1.02x faster                                                         |
| html5lib                   | 64.2 ms                                                | 63.2 ms: 1.02x faster                                                        |
| xml_etree_iterparse        | 101 ms                                                 | 99.7 ms: 1.02x faster                                                        |
| json_loads                 | 27.2 us                                                | 26.8 us: 1.01x faster                                                        |
| xml_etree_generate         | 86.7 ms                                                | 85.6 ms: 1.01x faster                                                        |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 570 ms: 1.01x faster                                                         |
| tomli_loads                | 2.14 sec                                               | 2.11 sec: 1.01x faster                                                       |
| pyflate                    | 471 ms                                                 | 466 ms: 1.01x faster                                                         |
| richards                   | 48.7 ms                                                | 48.2 ms: 1.01x faster                                                        |
| mdp                        | 2.72 sec                                               | 2.70 sec: 1.01x faster                                                       |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                                         |
| scimark_fft                | 364 ms                                                 | 366 ms: 1.00x slower                                                         |
| logging_silent             | 102 ns                                                 | 102 ns: 1.01x slower                                                         |
| regex_v8                   | 26.2 ms                                                | 26.4 ms: 1.01x slower                                                        |
| coverage                   | 84.0 ms                                                | 84.9 ms: 1.01x slower                                                        |
| typing_runtime_protocols   | 165 us                                                 | 167 us: 1.01x slower                                                         |
| python_startup_no_site     | 6.96 ms                                                | 7.05 ms: 1.01x slower                                                        |
| sympy_expand               | 463 ms                                                 | 470 ms: 1.01x slower                                                         |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 554 ms: 1.02x slower                                                         |
| unpickle_pure_python       | 216 us                                                 | 220 us: 1.02x slower                                                         |
| async_tree_io_tg           | 857 ms                                                 | 875 ms: 1.02x slower                                                         |
| bpe_tokeniser              | 4.75 sec                                               | 4.86 sec: 1.02x slower                                                       |
| coroutines                 | 22.7 ms                                                | 23.3 ms: 1.03x slower                                                        |
| raytrace                   | 267 ms                                                 | 275 ms: 1.03x slower                                                         |
| sympy_str                  | 275 ms                                                 | 284 ms: 1.03x slower                                                         |
| genshi_text                | 23.5 ms                                                | 24.3 ms: 1.03x slower                                                        |
| meteor_contest             | 109 ms                                                 | 113 ms: 1.04x slower                                                         |
| sqlglot_parse              | 1.27 ms                                                | 1.32 ms: 1.04x slower                                                        |
| docutils                   | 2.59 sec                                               | 2.70 sec: 1.04x slower                                                       |
| async_generators           | 436 ms                                                 | 454 ms: 1.04x slower                                                         |
| sympy_sum                  | 150 ms                                                 | 157 ms: 1.04x slower                                                         |
| async_tree_io              | 842 ms                                                 | 892 ms: 1.06x slower                                                         |
| pickle_pure_python         | 310 us                                                 | 331 us: 1.07x slower                                                         |
| dulwich_log                | 64.3 ms                                                | 69.2 ms: 1.08x slower                                                        |
| chaos                      | 58.1 ms                                                | 62.5 ms: 1.08x slower                                                        |
| sqlglot_normalize          | 108 ms                                                 | 116 ms: 1.08x slower                                                         |
| django_template            | 35.2 ms                                                | 38.4 ms: 1.09x slower                                                        |
| hexiom                     | 6.16 ms                                                | 6.81 ms: 1.10x slower                                                        |
| deltablue                  | 3.23 ms                                                | 3.58 ms: 1.11x slower                                                        |
| nqueens                    | 78.4 ms                                                | 87.5 ms: 1.12x slower                                                        |
| sqlglot_optimize           | 53.7 ms                                                | 60.1 ms: 1.12x slower                                                        |
| bench_thread_pool          | 822 us                                                 | 928 us: 1.13x slower                                                         |
| genshi_xml                 | 50.9 ms                                                | 57.8 ms: 1.14x slower                                                        |
| sqlglot_transpile          | 1.58 ms                                                | 1.83 ms: 1.16x slower                                                        |
| tornado_http               | 92.4 ms                                                | 110 ms: 1.19x slower                                                         |
| 2to3                       | 267 ms                                                 | 318 ms: 1.19x slower                                                         |
| pylint                     | 313 ms                                                 | 376 ms: 1.20x slower                                                         |
| generators                 | 29.0 ms                                                | 36.8 ms: 1.27x slower                                                        |
| sympy_integrate            | 19.9 ms                                                | 28.0 ms: 1.41x slower                                                        |
| Geometric mean             | (ref)                                                  | 1.00x faster                                                                 |

Benchmark hidden because not significant (7): pprint_pformat, comprehensions, scimark_lu, bench_mp_pool, logging_simple, asyncio_websockets, pprint_safe_repr
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20240919-3.14.0a0-99262b6-JIT/bm-20240919-linux-x86_64-savannahostrowski-jit_inv_cold_100-3.14.0a0-99262b6.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.005x faster
# HPT report

- Reliability score: 54.44% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.94x