# Results vs. base

- fork: brandtbucher
- ref: jit_cached_consts
- machine: linux-x86_64
- commit hash: 4953e8a
- commit date: 2025-03-28
- overall geometric mean: 1.011x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250317-linux-x86_64-python-fd545d735d5f9c048f99-3.14.0a6+-fd545d7 | bm-20250328-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a6+-4953e8a |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 263 ms                                                                 | 261 ms: 1.01x faster                                                      |
| docutils       | 2.68 sec                                                               | 2.66 sec: 1.01x faster                                                    |
| html5lib       | 62.2 ms                                                                | 61.7 ms: 1.01x faster                                                     |
| sphinx         | 1.03 sec                                                               | 1.02 sec: 1.01x faster                                                    |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250317-linux-x86_64-python-fd545d735d5f9c048f99-3.14.0a6+-fd545d7 | bm-20250328-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a6+-4953e8a |
|----------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed    | 497 ms                                                                 | 488 ms: 1.02x faster                                                      |
| async_tree_cpu_io_mixed_tg | 481 ms                                                                 | 473 ms: 1.02x faster                                                      |
| coroutines                 | 23.7 ms                                                                | 23.3 ms: 1.02x faster                                                     |
| async_tree_none            | 260 ms                                                                 | 256 ms: 1.01x faster                                                      |
| async_tree_memoization     | 319 ms                                                                 | 316 ms: 1.01x faster                                                      |
| async_tree_none_tg         | 251 ms                                                                 | 249 ms: 1.01x faster                                                      |
| async_generators           | 417 ms                                                                 | 419 ms: 1.01x slower                                                      |
| Geometric mean             | (ref)                                                                  | 1.01x faster                                                              |

Benchmark hidden because not significant (4): async_tree_memoization_tg, async_tree_io_tg, async_tree_io, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250317-linux-x86_64-python-fd545d735d5f9c048f99-3.14.0a6+-fd545d7 | bm-20250328-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a6+-4953e8a |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 65.0 ms                                                                | 64.6 ms: 1.01x faster                                                     |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                              |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250317-linux-x86_64-python-fd545d735d5f9c048f99-3.14.0a6+-fd545d7 | bm-20250328-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a6+-4953e8a |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_effbot   | 3.48 ms                                                                | 3.16 ms: 1.10x faster                                                     |
| regex_dna      | 225 ms                                                                 | 217 ms: 1.04x faster                                                      |
| regex_v8       | 23.9 ms                                                                | 23.1 ms: 1.04x faster                                                     |
| regex_compile  | 128 ms                                                                 | 127 ms: 1.01x faster                                                      |
| Geometric mean | (ref)                                                                  | 1.04x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250317-linux-x86_64-python-fd545d735d5f9c048f99-3.14.0a6+-fd545d7 | bm-20250328-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a6+-4953e8a |
|----------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| json_loads           | 30.2 us                                                                | 29.7 us: 1.02x faster                                                     |
| xml_etree_generate   | 80.4 ms                                                                | 79.2 ms: 1.02x faster                                                     |
| unpickle_pure_python | 216 us                                                                 | 212 us: 1.02x faster                                                      |
| xml_etree_process    | 56.2 ms                                                                | 55.4 ms: 1.02x faster                                                     |
| xml_etree_parse      | 142 ms                                                                 | 140 ms: 1.01x faster                                                      |
| xml_etree_iterparse  | 98.7 ms                                                                | 97.4 ms: 1.01x faster                                                     |
| pickle_pure_python   | 326 us                                                                 | 322 us: 1.01x faster                                                      |
| json_dumps           | 11.8 ms                                                                | 11.6 ms: 1.01x faster                                                     |
| tomli_loads          | 1.87 sec                                                               | 1.85 sec: 1.01x faster                                                    |
| Geometric mean       | (ref)                                                                  | 1.01x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250317-linux-x86_64-python-fd545d735d5f9c048f99-3.14.0a6+-fd545d7 | bm-20250328-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a6+-4953e8a |
|------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 8.22 ms                                                                | 8.19 ms: 1.00x faster                                                     |
| python_startup         | 13.1 ms                                                                | 13.1 ms: 1.00x faster                                                     |
| Geometric mean         | (ref)                                                                  | 1.00x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250317-linux-x86_64-python-fd545d735d5f9c048f99-3.14.0a6+-fd545d7 | bm-20250328-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a6+-4953e8a |
|-----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| genshi_text     | 21.6 ms                                                                | 20.8 ms: 1.04x faster                                                     |
| genshi_xml      | 51.0 ms                                                                | 49.7 ms: 1.03x faster                                                     |
| mako            | 11.1 ms                                                                | 10.9 ms: 1.02x faster                                                     |
| django_template | 31.9 ms                                                                | 31.6 ms: 1.01x faster                                                     |
| Geometric mean  | (ref)                                                                  | 1.02x faster                                                              |

All benchmarks:
===============

| Benchmark                  | bm-20250317-linux-x86_64-python-fd545d735d5f9c048f99-3.14.0a6+-fd545d7 | bm-20250328-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a6+-4953e8a |
|----------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_effbot               | 3.48 ms                                                                | 3.16 ms: 1.10x faster                                                     |
| pycparser                  | 1.18 sec                                                               | 1.12 sec: 1.06x faster                                                    |
| hexiom                     | 6.90 ms                                                                | 6.64 ms: 1.04x faster                                                     |
| regex_dna                  | 225 ms                                                                 | 217 ms: 1.04x faster                                                      |
| genshi_text                | 21.6 ms                                                                | 20.8 ms: 1.04x faster                                                     |
| regex_v8                   | 23.9 ms                                                                | 23.1 ms: 1.04x faster                                                     |
| scimark_sor                | 121 ms                                                                 | 117 ms: 1.03x faster                                                      |
| pyflate                    | 447 ms                                                                 | 433 ms: 1.03x faster                                                      |
| scimark_monte_carlo        | 68.9 ms                                                                | 66.8 ms: 1.03x faster                                                     |
| deltablue                  | 3.08 ms                                                                | 2.99 ms: 1.03x faster                                                     |
| logging_silent             | 100 ns                                                                 | 97.4 ns: 1.03x faster                                                     |
| richards_super             | 40.8 ms                                                                | 39.7 ms: 1.03x faster                                                     |
| genshi_xml                 | 51.0 ms                                                                | 49.7 ms: 1.03x faster                                                     |
| go                         | 129 ms                                                                 | 126 ms: 1.02x faster                                                      |
| sqlite_synth               | 2.75 us                                                                | 2.69 us: 1.02x faster                                                     |
| scimark_lu                 | 121 ms                                                                 | 119 ms: 1.02x faster                                                      |
| thrift                     | 779 us                                                                 | 764 us: 1.02x faster                                                      |
| deepcopy_memo              | 30.0 us                                                                | 29.5 us: 1.02x faster                                                     |
| chaos                      | 60.2 ms                                                                | 59.0 ms: 1.02x faster                                                     |
| richards                   | 35.6 ms                                                                | 34.9 ms: 1.02x faster                                                     |
| async_tree_cpu_io_mixed    | 497 ms                                                                 | 488 ms: 1.02x faster                                                      |
| async_tree_cpu_io_mixed_tg | 481 ms                                                                 | 473 ms: 1.02x faster                                                      |
| json                       | 5.36 ms                                                                | 5.26 ms: 1.02x faster                                                     |
| nqueens                    | 85.9 ms                                                                | 84.4 ms: 1.02x faster                                                     |
| coroutines                 | 23.7 ms                                                                | 23.3 ms: 1.02x faster                                                     |
| mako                       | 11.1 ms                                                                | 10.9 ms: 1.02x faster                                                     |
| json_loads                 | 30.2 us                                                                | 29.7 us: 1.02x faster                                                     |
| meteor_contest             | 110 ms                                                                 | 108 ms: 1.02x faster                                                      |
| xml_etree_generate         | 80.4 ms                                                                | 79.2 ms: 1.02x faster                                                     |
| unpickle_pure_python       | 216 us                                                                 | 212 us: 1.02x faster                                                      |
| xml_etree_process          | 56.2 ms                                                                | 55.4 ms: 1.02x faster                                                     |
| xml_etree_parse            | 142 ms                                                                 | 140 ms: 1.01x faster                                                      |
| sqlglot_v2_normalize       | 109 ms                                                                 | 107 ms: 1.01x faster                                                      |
| async_tree_none            | 260 ms                                                                 | 256 ms: 1.01x faster                                                      |
| spectral_norm              | 95.2 ms                                                                | 93.9 ms: 1.01x faster                                                     |
| raytrace                   | 270 ms                                                                 | 266 ms: 1.01x faster                                                      |
| xml_etree_iterparse        | 98.7 ms                                                                | 97.4 ms: 1.01x faster                                                     |
| pickle_pure_python         | 326 us                                                                 | 322 us: 1.01x faster                                                      |
| json_dumps                 | 11.8 ms                                                                | 11.6 ms: 1.01x faster                                                     |
| sqlalchemy_imperative      | 17.1 ms                                                                | 16.9 ms: 1.01x faster                                                     |
| sphinx                     | 1.03 sec                                                               | 1.02 sec: 1.01x faster                                                    |
| sqlglot_v2_transpile       | 1.61 ms                                                                | 1.60 ms: 1.01x faster                                                     |
| mdp                        | 2.50 sec                                                               | 2.48 sec: 1.01x faster                                                    |
| pprint_pformat             | 1.56 sec                                                               | 1.54 sec: 1.01x faster                                                    |
| deepcopy                   | 257 us                                                                 | 254 us: 1.01x faster                                                      |
| async_tree_memoization     | 319 ms                                                                 | 316 ms: 1.01x faster                                                      |
| generators                 | 28.3 ms                                                                | 28.1 ms: 1.01x faster                                                     |
| bpe_tokeniser              | 4.61 sec                                                               | 4.57 sec: 1.01x faster                                                    |
| async_tree_none_tg         | 251 ms                                                                 | 249 ms: 1.01x faster                                                      |
| docutils                   | 2.68 sec                                                               | 2.66 sec: 1.01x faster                                                    |
| html5lib                   | 62.2 ms                                                                | 61.7 ms: 1.01x faster                                                     |
| sympy_expand               | 474 ms                                                                 | 470 ms: 1.01x faster                                                      |
| bench_mp_pool              | 83.2 ms                                                                | 82.5 ms: 1.01x faster                                                     |
| pathlib                    | 16.7 ms                                                                | 16.6 ms: 1.01x faster                                                     |
| django_template            | 31.9 ms                                                                | 31.6 ms: 1.01x faster                                                     |
| sympy_integrate            | 20.3 ms                                                                | 20.1 ms: 1.01x faster                                                     |
| deepcopy_reduce            | 2.71 us                                                                | 2.69 us: 1.01x faster                                                     |
| sqlglot_v2_parse           | 1.30 ms                                                                | 1.29 ms: 1.01x faster                                                     |
| sqlglot_v2_optimize        | 54.2 ms                                                                | 53.8 ms: 1.01x faster                                                     |
| 2to3                       | 263 ms                                                                 | 261 ms: 1.01x faster                                                      |
| regex_compile              | 128 ms                                                                 | 127 ms: 1.01x faster                                                      |
| float                      | 65.0 ms                                                                | 64.6 ms: 1.01x faster                                                     |
| tomli_loads                | 1.87 sec                                                               | 1.85 sec: 1.01x faster                                                    |
| subparsers                 | 21.1 ms                                                                | 21.0 ms: 1.01x faster                                                     |
| shortest_path              | 498 ms                                                                 | 496 ms: 1.01x faster                                                      |
| connected_components       | 459 ms                                                                 | 457 ms: 1.00x faster                                                      |
| bench_thread_pool          | 883 us                                                                 | 879 us: 1.00x faster                                                      |
| python_startup_no_site     | 8.22 ms                                                                | 8.19 ms: 1.00x faster                                                     |
| python_startup             | 13.1 ms                                                                | 13.1 ms: 1.00x faster                                                     |
| sqlalchemy_declarative     | 133 ms                                                                 | 133 ms: 1.00x faster                                                      |
| sympy_str                  | 274 ms                                                                 | 273 ms: 1.00x faster                                                      |
| dulwich_log                | 60.2 ms                                                                | 60.4 ms: 1.00x slower                                                     |
| coverage                   | 84.5 ms                                                                | 84.8 ms: 1.00x slower                                                     |
| create_gc_cycles           | 2.49 ms                                                                | 2.50 ms: 1.00x slower                                                     |
| async_generators           | 417 ms                                                                 | 419 ms: 1.01x slower                                                      |
| scimark_fft                | 308 ms                                                                 | 309 ms: 1.01x slower                                                      |
| typing_runtime_protocols   | 170 us                                                                 | 172 us: 1.01x slower                                                      |
| gc_traversal               | 4.85 ms                                                                | 4.99 ms: 1.03x slower                                                     |
| Geometric mean             | (ref)                                                                  | 1.01x faster                                                              |

Benchmark hidden because not significant (18): async_tree_memoization_tg, async_tree_io_tg, pylint, telco, crypto_pyaes, async_tree_io, fannkuch, sympy_sum, k_core, pidigits, asyncio_websockets, scimark_sparse_mat_mult, many_optionals, logging_format, pprint_safe_repr, logging_simple, comprehensions, nbody

- Geometric mean (including insignificant results): 1.011x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x