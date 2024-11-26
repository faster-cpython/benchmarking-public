# Results vs. base

- fork: eendebakpt
- ref: int_freelist
- machine: darwin-arm64
- commit hash: d1e4aa2
- commit date: 2024-11-21
- overall geometric mean: 1.006x faster
- HPT reliability: 90.89%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241116-darwin-arm64-python-2313f8421080ceb3343c-3.14.0a1+-2313f84 | bm-20241121-darwin-arm64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| docutils       | 1.43 sec                                                               | 1.44 sec: 1.01x slower                                             |
| html5lib       | 31.2 ms                                                                | 30.9 ms: 1.01x faster                                              |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                       |

Benchmark hidden because not significant (2): 2to3, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark              | bm-20241116-darwin-arm64-python-2313f8421080ceb3343c-3.14.0a1+-2313f84 | bm-20241121-darwin-arm64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_eager_io_tg | 727 ms                                                                 | 708 ms: 1.03x faster                                               |
| async_tree_none_tg     | 207 ms                                                                 | 203 ms: 1.02x faster                                               |
| async_tree_none        | 207 ms                                                                 | 203 ms: 1.02x faster                                               |
| async_tree_io_tg       | 624 ms                                                                 | 613 ms: 1.02x faster                                               |
| async_generators       | 284 ms                                                                 | 281 ms: 1.01x faster                                               |
| coroutines             | 17.6 ms                                                                | 17.4 ms: 1.01x faster                                              |
| async_tree_eager_tg    | 44.2 ms                                                                | 44.6 ms: 1.01x slower                                              |
| Geometric mean         | (ref)                                                                  | 1.01x faster                                                       |

Benchmark hidden because not significant (12): async_tree_eager_io, async_tree_io, async_tree_memoization, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, async_tree_eager_memoization_tg, async_tree_eager_memoization, async_tree_eager_cpu_io_mixed, async_tree_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241116-darwin-arm64-python-2313f8421080ceb3343c-3.14.0a1+-2313f84 | bm-20241121-darwin-arm64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| float          | 52.7 ms                                                                | 52.5 ms: 1.00x faster                                              |
| nbody          | 68.1 ms                                                                | 68.2 ms: 1.00x slower                                              |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                       |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241116-darwin-arm64-python-2313f8421080ceb3343c-3.14.0a1+-2313f84 | bm-20241121-darwin-arm64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_compile  | 71.9 ms                                                                | 70.6 ms: 1.02x faster                                              |
| regex_effbot   | 2.31 ms                                                                | 2.29 ms: 1.01x faster                                              |
| regex_dna      | 135 ms                                                                 | 135 ms: 1.00x slower                                               |
| regex_v8       | 15.7 ms                                                                | 15.8 ms: 1.00x slower                                              |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241116-darwin-arm64-python-2313f8421080ceb3343c-3.14.0a1+-2313f84 | bm-20241121-darwin-arm64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|----------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| tomli_loads          | 1.53 sec                                                               | 1.47 sec: 1.04x faster                                             |
| unpickle_pure_python | 153 us                                                                 | 153 us: 1.00x slower                                               |
| json_dumps           | 7.26 ms                                                                | 7.29 ms: 1.00x slower                                              |
| xml_etree_generate   | 53.8 ms                                                                | 54.2 ms: 1.01x slower                                              |
| xml_etree_process    | 38.8 ms                                                                | 39.5 ms: 1.02x slower                                              |
| Geometric mean       | (ref)                                                                  | 1.00x faster                                                       |

Benchmark hidden because not significant (4): xml_etree_parse, xml_etree_iterparse, pickle_pure_python, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241116-darwin-arm64-python-2313f8421080ceb3343c-3.14.0a1+-2313f84 | bm-20241121-darwin-arm64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup_no_site | 14.8 ms                                                                | 13.9 ms: 1.07x faster                                              |
| Geometric mean         | (ref)                                                                  | 1.03x faster                                                       |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241116-darwin-arm64-python-2313f8421080ceb3343c-3.14.0a1+-2313f84 | bm-20241121-darwin-arm64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|-----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| django_template | 21.0 ms                                                                | 20.9 ms: 1.00x faster                                              |
| mako            | 6.90 ms                                                                | 6.92 ms: 1.00x slower                                              |
| genshi_text     | 14.3 ms                                                                | 14.4 ms: 1.01x slower                                              |
| Geometric mean  | (ref)                                                                  | 1.00x slower                                                       |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark               | bm-20241116-darwin-arm64-python-2313f8421080ceb3343c-3.14.0a1+-2313f84 | bm-20241121-darwin-arm64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|-------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| spectral_norm           | 71.7 ms                                                                | 62.1 ms: 1.16x faster                                              |
| scimark_sparse_mat_mult | 2.97 ms                                                                | 2.67 ms: 1.11x faster                                              |
| scimark_fft             | 193 ms                                                                 | 173 ms: 1.11x faster                                               |
| python_startup_no_site  | 14.8 ms                                                                | 13.9 ms: 1.07x faster                                              |
| scimark_sor             | 99.9 ms                                                                | 95.4 ms: 1.05x faster                                              |
| tomli_loads             | 1.53 sec                                                               | 1.47 sec: 1.04x faster                                             |
| pyflate                 | 337 ms                                                                 | 326 ms: 1.03x faster                                               |
| async_tree_eager_io_tg  | 727 ms                                                                 | 708 ms: 1.03x faster                                               |
| async_tree_none_tg      | 207 ms                                                                 | 203 ms: 1.02x faster                                               |
| pprint_safe_repr        | 492 ms                                                                 | 482 ms: 1.02x faster                                               |
| regex_compile           | 71.9 ms                                                                | 70.6 ms: 1.02x faster                                              |
| deepcopy_memo           | 18.7 us                                                                | 18.4 us: 1.02x faster                                              |
| sqlite_synth            | 1.55 us                                                                | 1.52 us: 1.02x faster                                              |
| async_tree_none         | 207 ms                                                                 | 203 ms: 1.02x faster                                               |
| async_tree_io_tg        | 624 ms                                                                 | 613 ms: 1.02x faster                                               |
| scimark_monte_carlo     | 46.1 ms                                                                | 45.3 ms: 1.02x faster                                              |
| deltablue               | 2.47 ms                                                                | 2.45 ms: 1.01x faster                                              |
| async_generators        | 284 ms                                                                 | 281 ms: 1.01x faster                                               |
| regex_effbot            | 2.31 ms                                                                | 2.29 ms: 1.01x faster                                              |
| coroutines              | 17.6 ms                                                                | 17.4 ms: 1.01x faster                                              |
| sqlglot_transpile       | 974 us                                                                 | 966 us: 1.01x faster                                               |
| html5lib                | 31.2 ms                                                                | 30.9 ms: 1.01x faster                                              |
| dulwich_log             | 28.0 ms                                                                | 27.8 ms: 1.01x faster                                              |
| logging_simple          | 3.28 us                                                                | 3.26 us: 1.01x faster                                              |
| coverage                | 44.5 ms                                                                | 44.2 ms: 1.01x faster                                              |
| raytrace                | 170 ms                                                                 | 169 ms: 1.01x faster                                               |
| logging_silent          | 68.3 ns                                                                | 67.9 ns: 1.01x faster                                              |
| sqlglot_parse           | 799 us                                                                 | 794 us: 1.01x faster                                               |
| go                      | 87.7 ms                                                                | 87.3 ms: 1.00x faster                                              |
| logging_format          | 3.59 us                                                                | 3.58 us: 1.00x faster                                              |
| float                   | 52.7 ms                                                                | 52.5 ms: 1.00x faster                                              |
| django_template         | 21.0 ms                                                                | 20.9 ms: 1.00x faster                                              |
| nqueens                 | 57.6 ms                                                                | 57.4 ms: 1.00x faster                                              |
| meteor_contest          | 73.0 ms                                                                | 72.7 ms: 1.00x faster                                              |
| hexiom                  | 4.47 ms                                                                | 4.47 ms: 1.00x faster                                              |
| unpickle_pure_python    | 153 us                                                                 | 153 us: 1.00x slower                                               |
| nbody                   | 68.1 ms                                                                | 68.2 ms: 1.00x slower                                              |
| mako                    | 6.90 ms                                                                | 6.92 ms: 1.00x slower                                              |
| bpe_tokeniser           | 3.17 sec                                                               | 3.18 sec: 1.00x slower                                             |
| mdp                     | 1.50 sec                                                               | 1.51 sec: 1.00x slower                                             |
| regex_dna               | 135 ms                                                                 | 135 ms: 1.00x slower                                               |
| sqlalchemy_declarative  | 58.2 ms                                                                | 58.5 ms: 1.00x slower                                              |
| json_dumps              | 7.26 ms                                                                | 7.29 ms: 1.00x slower                                              |
| sympy_expand            | 235 ms                                                                 | 235 ms: 1.00x slower                                               |
| regex_v8                | 15.7 ms                                                                | 15.8 ms: 1.00x slower                                              |
| telco                   | 4.50 ms                                                                | 4.53 ms: 1.01x slower                                              |
| docutils                | 1.43 sec                                                               | 1.44 sec: 1.01x slower                                             |
| genshi_text             | 14.3 ms                                                                | 14.4 ms: 1.01x slower                                              |
| crypto_pyaes            | 53.7 ms                                                                | 54.1 ms: 1.01x slower                                              |
| sympy_str               | 139 ms                                                                 | 140 ms: 1.01x slower                                               |
| json                    | 2.87 ms                                                                | 2.89 ms: 1.01x slower                                              |
| many_optionals          | 358 us                                                                 | 361 us: 1.01x slower                                               |
| sqlglot_normalize       | 176 ms                                                                 | 177 ms: 1.01x slower                                               |
| deepcopy                | 153 us                                                                 | 154 us: 1.01x slower                                               |
| async_tree_eager_tg     | 44.2 ms                                                                | 44.6 ms: 1.01x slower                                              |
| fannkuch                | 266 ms                                                                 | 268 ms: 1.01x slower                                               |
| sympy_sum               | 72.1 ms                                                                | 72.7 ms: 1.01x slower                                              |
| sqlglot_optimize        | 32.9 ms                                                                | 33.2 ms: 1.01x slower                                              |
| connected_components    | 319 ms                                                                 | 321 ms: 1.01x slower                                               |
| sympy_integrate         | 11.4 ms                                                                | 11.5 ms: 1.01x slower                                              |
| xml_etree_generate      | 53.8 ms                                                                | 54.2 ms: 1.01x slower                                              |
| shortest_path           | 345 ms                                                                 | 348 ms: 1.01x slower                                               |
| sqlalchemy_imperative   | 6.43 ms                                                                | 6.52 ms: 1.01x slower                                              |
| thrift                  | 430 us                                                                 | 436 us: 1.01x slower                                               |
| richards                | 33.3 ms                                                                | 33.7 ms: 1.01x slower                                              |
| richards_super          | 36.7 ms                                                                | 37.2 ms: 1.02x slower                                              |
| bench_thread_pool       | 465 us                                                                 | 473 us: 1.02x slower                                               |
| xml_etree_process       | 38.8 ms                                                                | 39.5 ms: 1.02x slower                                              |
| chaos                   | 39.3 ms                                                                | 40.5 ms: 1.03x slower                                              |
| Geometric mean          | (ref)                                                                  | 1.01x faster                                                       |

Benchmark hidden because not significant (35): async_tree_eager_io, async_tree_io, async_tree_memoization, async_tree_memoization_tg, k_core, async_tree_cpu_io_mixed_tg, async_tree_eager_memoization_tg, xml_etree_parse, bench_mp_pool, xml_etree_iterparse, subparsers, async_tree_eager_memoization, genshi_xml, generators, async_tree_eager_cpu_io_mixed, async_tree_cpu_io_mixed, 2to3, async_tree_eager_cpu_io_mixed_tg, create_gc_cycles, comprehensions, async_tree_eager, pidigits, pickle_pure_python, pycparser, pprint_pformat, scimark_lu, gc_traversal, deepcopy_reduce, pylint, asyncio_websockets, json_loads, python_startup, typing_runtime_protocols, sphinx, pathlib

- Geometric mean (including insignificant results): 1.006x faster
# HPT report

- Reliability score: 90.89% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x