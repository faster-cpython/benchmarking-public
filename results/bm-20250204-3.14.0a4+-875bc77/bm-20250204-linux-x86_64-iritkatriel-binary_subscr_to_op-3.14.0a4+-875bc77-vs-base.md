# Results vs. base

- fork: iritkatriel
- ref: binary_subscr_to_op
- machine: linux-x86_64
- commit hash: 875bc77
- commit date: 2025-02-04
- overall geometric mean: 1.001x faster
- HPT reliability: 90.06%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250204-linux-x86_64-python-d3c54f37889436ded452-3.14.0a4+-d3c54f3 | bm-20250204-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-875bc77 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 251 ms                                                                 | 250 ms: 1.00x faster                                                       |
| docutils       | 2.58 sec                                                               | 2.57 sec: 1.00x faster                                                     |
| html5lib       | 60.5 ms                                                                | 61.3 ms: 1.01x slower                                                      |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                               |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250204-linux-x86_64-python-d3c54f37889436ded452-3.14.0a4+-d3c54f3 | bm-20250204-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-875bc77 |
|----------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_generators           | 388 ms                                                                 | 380 ms: 1.02x faster                                                       |
| async_tree_cpu_io_mixed_tg | 489 ms                                                                 | 492 ms: 1.01x slower                                                       |
| async_tree_cpu_io_mixed    | 498 ms                                                                 | 502 ms: 1.01x slower                                                       |
| coroutines                 | 23.2 ms                                                                | 23.5 ms: 1.01x slower                                                      |
| async_tree_none_tg         | 254 ms                                                                 | 258 ms: 1.02x slower                                                       |
| async_tree_memoization     | 322 ms                                                                 | 327 ms: 1.02x slower                                                       |
| Geometric mean             | (ref)                                                                  | 1.01x slower                                                               |

Benchmark hidden because not significant (5): asyncio_websockets, async_tree_io_tg, async_tree_none, async_tree_io, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250204-linux-x86_64-python-d3c54f37889436ded452-3.14.0a4+-d3c54f3 | bm-20250204-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-875bc77 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 70.3 ms                                                                | 68.5 ms: 1.03x faster                                                      |
| nbody          | 94.1 ms                                                                | 92.1 ms: 1.02x faster                                                      |
| pidigits       | 187 ms                                                                 | 186 ms: 1.00x faster                                                       |
| Geometric mean | (ref)                                                                  | 1.02x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250204-linux-x86_64-python-d3c54f37889436ded452-3.14.0a4+-d3c54f3 | bm-20250204-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-875bc77 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 125 ms                                                                 | 124 ms: 1.01x faster                                                       |
| regex_effbot   | 3.29 ms                                                                | 3.27 ms: 1.00x faster                                                      |
| regex_v8       | 25.5 ms                                                                | 25.6 ms: 1.00x slower                                                      |
| regex_dna      | 204 ms                                                                 | 219 ms: 1.07x slower                                                       |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250204-linux-x86_64-python-d3c54f37889436ded452-3.14.0a4+-d3c54f3 | bm-20250204-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-875bc77 |
|----------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pickle_pure_python   | 318 us                                                                 | 312 us: 1.02x faster                                                       |
| tomli_loads          | 1.96 sec                                                               | 1.93 sec: 1.02x faster                                                     |
| unpickle_pure_python | 216 us                                                                 | 214 us: 1.01x faster                                                       |
| xml_etree_generate   | 83.1 ms                                                                | 82.6 ms: 1.01x faster                                                      |
| xml_etree_parse      | 140 ms                                                                 | 139 ms: 1.01x faster                                                       |
| json_dumps           | 11.7 ms                                                                | 11.8 ms: 1.01x slower                                                      |
| Geometric mean       | (ref)                                                                  | 1.01x faster                                                               |

Benchmark hidden because not significant (3): xml_etree_iterparse, xml_etree_process, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250204-linux-x86_64-python-d3c54f37889436ded452-3.14.0a4+-d3c54f3 | bm-20250204-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-875bc77 |
|------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 7.02 ms                                                                | 7.03 ms: 1.00x slower                                                      |
| python_startup         | 12.8 ms                                                                | 12.8 ms: 1.01x slower                                                      |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250204-linux-x86_64-python-d3c54f37889436ded452-3.14.0a4+-d3c54f3 | bm-20250204-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-875bc77 |
|-----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_xml      | 48.7 ms                                                                | 47.7 ms: 1.02x faster                                                      |
| genshi_text     | 21.4 ms                                                                | 21.2 ms: 1.01x faster                                                      |
| django_template | 31.5 ms                                                                | 31.4 ms: 1.00x faster                                                      |
| mako            | 11.2 ms                                                                | 11.3 ms: 1.01x slower                                                      |
| Geometric mean  | (ref)                                                                  | 1.01x faster                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20250204-linux-x86_64-python-d3c54f37889436ded452-3.14.0a4+-d3c54f3 | bm-20250204-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-875bc77 |
|----------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pycparser                  | 1.17 sec                                                               | 1.11 sec: 1.05x faster                                                     |
| logging_silent             | 105 ns                                                                 | 101 ns: 1.04x faster                                                       |
| deepcopy_memo              | 30.1 us                                                                | 29.3 us: 1.03x faster                                                      |
| float                      | 70.3 ms                                                                | 68.5 ms: 1.03x faster                                                      |
| hexiom                     | 6.21 ms                                                                | 6.05 ms: 1.03x faster                                                      |
| fannkuch                   | 403 ms                                                                 | 394 ms: 1.02x faster                                                       |
| nbody                      | 94.1 ms                                                                | 92.1 ms: 1.02x faster                                                      |
| genshi_xml                 | 48.7 ms                                                                | 47.7 ms: 1.02x faster                                                      |
| async_generators           | 388 ms                                                                 | 380 ms: 1.02x faster                                                       |
| pickle_pure_python         | 318 us                                                                 | 312 us: 1.02x faster                                                       |
| scimark_monte_carlo        | 67.4 ms                                                                | 66.2 ms: 1.02x faster                                                      |
| scimark_fft                | 346 ms                                                                 | 340 ms: 1.02x faster                                                       |
| deltablue                  | 3.20 ms                                                                | 3.15 ms: 1.02x faster                                                      |
| deepcopy                   | 254 us                                                                 | 250 us: 1.02x faster                                                       |
| tomli_loads                | 1.96 sec                                                               | 1.93 sec: 1.02x faster                                                     |
| crypto_pyaes               | 70.9 ms                                                                | 69.9 ms: 1.01x faster                                                      |
| comprehensions             | 16.4 us                                                                | 16.2 us: 1.01x faster                                                      |
| nqueens                    | 79.9 ms                                                                | 78.9 ms: 1.01x faster                                                      |
| scimark_lu                 | 116 ms                                                                 | 114 ms: 1.01x faster                                                       |
| json                       | 5.19 ms                                                                | 5.13 ms: 1.01x faster                                                      |
| genshi_text                | 21.4 ms                                                                | 21.2 ms: 1.01x faster                                                      |
| unpickle_pure_python       | 216 us                                                                 | 214 us: 1.01x faster                                                       |
| regex_compile              | 125 ms                                                                 | 124 ms: 1.01x faster                                                       |
| bpe_tokeniser              | 4.42 sec                                                               | 4.38 sec: 1.01x faster                                                     |
| sqlglot_normalize          | 103 ms                                                                 | 103 ms: 1.01x faster                                                       |
| sqlalchemy_imperative      | 16.4 ms                                                                | 16.2 ms: 1.01x faster                                                      |
| coverage                   | 90.3 ms                                                                | 89.7 ms: 1.01x faster                                                      |
| generators                 | 28.0 ms                                                                | 27.8 ms: 1.01x faster                                                      |
| raytrace                   | 269 ms                                                                 | 268 ms: 1.01x faster                                                       |
| sympy_integrate            | 19.5 ms                                                                | 19.4 ms: 1.01x faster                                                      |
| sqlglot_parse              | 1.24 ms                                                                | 1.24 ms: 1.01x faster                                                      |
| sqlglot_optimize           | 51.7 ms                                                                | 51.4 ms: 1.01x faster                                                      |
| xml_etree_generate         | 83.1 ms                                                                | 82.6 ms: 1.01x faster                                                      |
| xml_etree_parse            | 140 ms                                                                 | 139 ms: 1.01x faster                                                       |
| regex_effbot               | 3.29 ms                                                                | 3.27 ms: 1.00x faster                                                      |
| pidigits                   | 187 ms                                                                 | 186 ms: 1.00x faster                                                       |
| 2to3                       | 251 ms                                                                 | 250 ms: 1.00x faster                                                       |
| django_template            | 31.5 ms                                                                | 31.4 ms: 1.00x faster                                                      |
| chaos                      | 58.1 ms                                                                | 57.9 ms: 1.00x faster                                                      |
| sqlalchemy_declarative     | 128 ms                                                                 | 128 ms: 1.00x faster                                                       |
| docutils                   | 2.58 sec                                                               | 2.57 sec: 1.00x faster                                                     |
| gc_traversal               | 5.02 ms                                                                | 5.03 ms: 1.00x slower                                                      |
| python_startup_no_site     | 7.02 ms                                                                | 7.03 ms: 1.00x slower                                                      |
| regex_v8                   | 25.5 ms                                                                | 25.6 ms: 1.00x slower                                                      |
| pprint_safe_repr           | 703 ms                                                                 | 707 ms: 1.01x slower                                                       |
| python_startup             | 12.8 ms                                                                | 12.8 ms: 1.01x slower                                                      |
| json_dumps                 | 11.7 ms                                                                | 11.8 ms: 1.01x slower                                                      |
| richards                   | 43.8 ms                                                                | 44.1 ms: 1.01x slower                                                      |
| mako                       | 11.2 ms                                                                | 11.3 ms: 1.01x slower                                                      |
| async_tree_cpu_io_mixed_tg | 489 ms                                                                 | 492 ms: 1.01x slower                                                       |
| sympy_sum                  | 145 ms                                                                 | 146 ms: 1.01x slower                                                       |
| async_tree_cpu_io_mixed    | 498 ms                                                                 | 502 ms: 1.01x slower                                                       |
| dulwich_log                | 63.3 ms                                                                | 63.8 ms: 1.01x slower                                                      |
| pprint_pformat             | 1.45 sec                                                               | 1.46 sec: 1.01x slower                                                     |
| typing_runtime_protocols   | 156 us                                                                 | 157 us: 1.01x slower                                                       |
| meteor_contest             | 104 ms                                                                 | 106 ms: 1.01x slower                                                       |
| deepcopy_reduce            | 2.63 us                                                                | 2.66 us: 1.01x slower                                                      |
| html5lib                   | 60.5 ms                                                                | 61.3 ms: 1.01x slower                                                      |
| subparsers                 | 20.3 ms                                                                | 20.6 ms: 1.01x slower                                                      |
| richards_super             | 49.8 ms                                                                | 50.5 ms: 1.01x slower                                                      |
| coroutines                 | 23.2 ms                                                                | 23.5 ms: 1.01x slower                                                      |
| async_tree_none_tg         | 254 ms                                                                 | 258 ms: 1.02x slower                                                       |
| async_tree_memoization     | 322 ms                                                                 | 327 ms: 1.02x slower                                                       |
| logging_format             | 6.04 us                                                                | 6.14 us: 1.02x slower                                                      |
| logging_simple             | 5.42 us                                                                | 5.51 us: 1.02x slower                                                      |
| telco                      | 7.80 ms                                                                | 7.98 ms: 1.02x slower                                                      |
| spectral_norm              | 94.1 ms                                                                | 97.0 ms: 1.03x slower                                                      |
| pyflate                    | 443 ms                                                                 | 460 ms: 1.04x slower                                                       |
| regex_dna                  | 204 ms                                                                 | 219 ms: 1.07x slower                                                       |
| Geometric mean             | (ref)                                                                  | 1.00x faster                                                               |

Benchmark hidden because not significant (27): k_core, pylint, sqlite_synth, mdp, xml_etree_iterparse, sqlglot_transpile, bench_thread_pool, bench_mp_pool, xml_etree_process, scimark_sparse_mat_mult, scimark_sor, go, pathlib, create_gc_cycles, connected_components, sympy_expand, sympy_str, many_optionals, json_loads, asyncio_websockets, thrift, async_tree_io_tg, shortest_path, sphinx, async_tree_none, async_tree_io, async_tree_memoization_tg

- Geometric mean (including insignificant results): 1.001x faster

# HPT report

- Reliability score: 90.06% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x