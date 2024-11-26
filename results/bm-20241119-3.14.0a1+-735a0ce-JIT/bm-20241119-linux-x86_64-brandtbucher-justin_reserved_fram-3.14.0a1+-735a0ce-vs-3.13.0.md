# Results vs. 3.13.0

- fork: brandtbucher
- ref: justin_reserved_fram
- machine: linux-x86_64
- commit hash: 735a0ce
- commit date: 2024-11-19
- overall geometric mean: 1.004x slower
- HPT reliability: 94.22%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241119-linux-x86_64-brandtbucher-justin_reserved_fram-3.14.0a1+-735a0ce |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 279 ms: 1.05x slower                                                         |
| docutils       | 2.59 sec                                               | 2.93 sec: 1.13x slower                                                       |
| html5lib       | 64.2 ms                                                | 65.7 ms: 1.02x slower                                                        |
| sphinx         | 1.03 sec                                               | 1.18 sec: 1.14x slower                                                       |
| Geometric mean | (ref)                                                  | 1.08x slower                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241119-linux-x86_64-brandtbucher-justin_reserved_fram-3.14.0a1+-735a0ce |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 464 ms                                                 | 379 ms: 1.22x faster                                                         |
| async_tree_memoization     | 442 ms                                                 | 420 ms: 1.05x faster                                                         |
| async_tree_none            | 351 ms                                                 | 334 ms: 1.05x faster                                                         |
| async_tree_io              | 842 ms                                                 | 864 ms: 1.03x slower                                                         |
| async_generators           | 436 ms                                                 | 454 ms: 1.04x slower                                                         |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 572 ms: 1.05x slower                                                         |
| async_tree_io_tg           | 857 ms                                                 | 986 ms: 1.15x slower                                                         |
| Geometric mean             | (ref)                                                  | 1.00x faster                                                                 |

Benchmark hidden because not significant (4): coroutines, asyncio_websockets, async_tree_none_tg, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241119-linux-x86_64-brandtbucher-justin_reserved_fram-3.14.0a1+-735a0ce |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 87.0 ms                                                | 82.4 ms: 1.06x faster                                                        |
| float          | 79.2 ms                                                | 76.6 ms: 1.03x faster                                                        |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x slower                                                         |
| Geometric mean | (ref)                                                  | 1.03x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241119-linux-x86_64-brandtbucher-justin_reserved_fram-3.14.0a1+-735a0ce |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                | 25.4 ms: 1.03x faster                                                        |
| regex_effbot   | 3.73 ms                                                | 3.65 ms: 1.02x faster                                                        |
| regex_compile  | 132 ms                                                 | 139 ms: 1.05x slower                                                         |
| Geometric mean | (ref)                                                  | 1.00x faster                                                                 |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241119-linux-x86_64-brandtbucher-justin_reserved_fram-3.14.0a1+-735a0ce |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_generate   | 86.7 ms                                                | 79.1 ms: 1.10x faster                                                        |
| xml_etree_process    | 60.6 ms                                                | 55.7 ms: 1.09x faster                                                        |
| tomli_loads          | 2.14 sec                                               | 1.97 sec: 1.08x faster                                                       |
| xml_etree_parse      | 156 ms                                                 | 149 ms: 1.05x faster                                                         |
| json_loads           | 27.2 us                                                | 26.7 us: 1.02x faster                                                        |
| unpickle_pure_python | 216 us                                                 | 218 us: 1.01x slower                                                         |
| json_dumps           | 10.6 ms                                                | 11.1 ms: 1.05x slower                                                        |
| pickle_pure_python   | 310 us                                                 | 325 us: 1.05x slower                                                         |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                                 |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241119-linux-x86_64-brandtbucher-justin_reserved_fram-3.14.0a1+-735a0ce |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 6.96 ms                                                | 7.11 ms: 1.02x slower                                                        |
| python_startup         | 12.5 ms                                                | 12.8 ms: 1.03x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241119-linux-x86_64-brandtbucher-justin_reserved_fram-3.14.0a1+-735a0ce |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 10.1 ms: 1.09x faster                                                        |
| django_template | 35.2 ms                                                | 33.9 ms: 1.04x faster                                                        |
| genshi_text     | 23.5 ms                                                | 25.0 ms: 1.06x slower                                                        |
| genshi_xml      | 50.9 ms                                                | 58.8 ms: 1.15x slower                                                        |
| Geometric mean  | (ref)                                                  | 1.02x slower                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241119-linux-x86_64-brandtbucher-justin_reserved_fram-3.14.0a1+-735a0ce |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| deepcopy                   | 358 us                                                 | 272 us: 1.32x faster                                                         |
| deepcopy_memo              | 39.1 us                                                | 29.9 us: 1.31x faster                                                        |
| richards                   | 48.7 ms                                                | 39.1 ms: 1.24x faster                                                        |
| async_tree_memoization_tg  | 464 ms                                                 | 379 ms: 1.22x faster                                                         |
| richards_super             | 54.9 ms                                                | 45.1 ms: 1.22x faster                                                        |
| deepcopy_reduce            | 3.20 us                                                | 2.69 us: 1.19x faster                                                        |
| scimark_fft                | 364 ms                                                 | 322 ms: 1.13x faster                                                         |
| telco                      | 8.54 ms                                                | 7.69 ms: 1.11x faster                                                        |
| xml_etree_generate         | 86.7 ms                                                | 79.1 ms: 1.10x faster                                                        |
| pathlib                    | 17.5 ms                                                | 16.0 ms: 1.10x faster                                                        |
| mako                       | 11.1 ms                                                | 10.1 ms: 1.09x faster                                                        |
| crypto_pyaes               | 75.3 ms                                                | 68.9 ms: 1.09x faster                                                        |
| xml_etree_process          | 60.6 ms                                                | 55.7 ms: 1.09x faster                                                        |
| scimark_sparse_mat_mult    | 5.04 ms                                                | 4.65 ms: 1.09x faster                                                        |
| tomli_loads                | 2.14 sec                                               | 1.97 sec: 1.08x faster                                                       |
| go                         | 144 ms                                                 | 134 ms: 1.08x faster                                                         |
| json                       | 5.36 ms                                                | 4.98 ms: 1.08x faster                                                        |
| pyflate                    | 471 ms                                                 | 443 ms: 1.06x faster                                                         |
| bpe_tokeniser              | 4.75 sec                                               | 4.48 sec: 1.06x faster                                                       |
| logging_silent             | 102 ns                                                 | 96.3 ns: 1.06x faster                                                        |
| nbody                      | 87.0 ms                                                | 82.4 ms: 1.06x faster                                                        |
| mdp                        | 2.72 sec                                               | 2.58 sec: 1.05x faster                                                       |
| async_tree_memoization     | 442 ms                                                 | 420 ms: 1.05x faster                                                         |
| async_tree_none            | 351 ms                                                 | 334 ms: 1.05x faster                                                         |
| xml_etree_parse            | 156 ms                                                 | 149 ms: 1.05x faster                                                         |
| scimark_monte_carlo        | 67.4 ms                                                | 64.5 ms: 1.05x faster                                                        |
| scimark_sor                | 124 ms                                                 | 118 ms: 1.04x faster                                                         |
| logging_format             | 6.40 us                                                | 6.15 us: 1.04x faster                                                        |
| django_template            | 35.2 ms                                                | 33.9 ms: 1.04x faster                                                        |
| fannkuch                   | 404 ms                                                 | 390 ms: 1.04x faster                                                         |
| regex_v8                   | 26.2 ms                                                | 25.4 ms: 1.03x faster                                                        |
| float                      | 79.2 ms                                                | 76.6 ms: 1.03x faster                                                        |
| logging_simple             | 5.72 us                                                | 5.56 us: 1.03x faster                                                        |
| regex_effbot               | 3.73 ms                                                | 3.65 ms: 1.02x faster                                                        |
| json_loads                 | 27.2 us                                                | 26.7 us: 1.02x faster                                                        |
| thrift                     | 809 us                                                 | 795 us: 1.02x faster                                                         |
| meteor_contest             | 109 ms                                                 | 107 ms: 1.02x faster                                                         |
| connected_components       | 444 ms                                                 | 438 ms: 1.01x faster                                                         |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x slower                                                         |
| unpickle_pure_python       | 216 us                                                 | 218 us: 1.01x slower                                                         |
| pprint_pformat             | 1.49 sec                                               | 1.52 sec: 1.02x slower                                                       |
| deltablue                  | 3.23 ms                                                | 3.28 ms: 1.02x slower                                                        |
| pprint_safe_repr           | 728 ms                                                 | 743 ms: 1.02x slower                                                         |
| python_startup_no_site     | 6.96 ms                                                | 7.11 ms: 1.02x slower                                                        |
| scimark_lu                 | 113 ms                                                 | 115 ms: 1.02x slower                                                         |
| spectral_norm              | 115 ms                                                 | 118 ms: 1.02x slower                                                         |
| html5lib                   | 64.2 ms                                                | 65.7 ms: 1.02x slower                                                        |
| chaos                      | 58.1 ms                                                | 59.6 ms: 1.03x slower                                                        |
| python_startup             | 12.5 ms                                                | 12.8 ms: 1.03x slower                                                        |
| async_tree_io              | 842 ms                                                 | 864 ms: 1.03x slower                                                         |
| raytrace                   | 267 ms                                                 | 276 ms: 1.03x slower                                                         |
| typing_runtime_protocols   | 165 us                                                 | 171 us: 1.04x slower                                                         |
| sqlalchemy_imperative      | 17.1 ms                                                | 17.7 ms: 1.04x slower                                                        |
| comprehensions             | 16.5 us                                                | 17.1 us: 1.04x slower                                                        |
| async_generators           | 436 ms                                                 | 454 ms: 1.04x slower                                                         |
| sqlglot_parse              | 1.27 ms                                                | 1.33 ms: 1.04x slower                                                        |
| gc_traversal               | 4.37 ms                                                | 4.57 ms: 1.04x slower                                                        |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 572 ms: 1.05x slower                                                         |
| 2to3                       | 267 ms                                                 | 279 ms: 1.05x slower                                                         |
| json_dumps                 | 10.6 ms                                                | 11.1 ms: 1.05x slower                                                        |
| pickle_pure_python         | 310 us                                                 | 325 us: 1.05x slower                                                         |
| regex_compile              | 132 ms                                                 | 139 ms: 1.05x slower                                                         |
| dulwich_log                | 64.3 ms                                                | 67.8 ms: 1.05x slower                                                        |
| genshi_text                | 23.5 ms                                                | 25.0 ms: 1.06x slower                                                        |
| sqlglot_transpile          | 1.58 ms                                                | 1.70 ms: 1.07x slower                                                        |
| sqlglot_normalize          | 108 ms                                                 | 116 ms: 1.08x slower                                                         |
| bench_thread_pool          | 822 us                                                 | 888 us: 1.08x slower                                                         |
| sympy_expand               | 463 ms                                                 | 504 ms: 1.09x slower                                                         |
| sqlalchemy_declarative     | 133 ms                                                 | 147 ms: 1.10x slower                                                         |
| sympy_str                  | 275 ms                                                 | 304 ms: 1.11x slower                                                         |
| create_gc_cycles           | 2.41 ms                                                | 2.69 ms: 1.12x slower                                                        |
| nqueens                    | 78.4 ms                                                | 87.9 ms: 1.12x slower                                                        |
| sqlglot_optimize           | 53.7 ms                                                | 60.4 ms: 1.12x slower                                                        |
| docutils                   | 2.59 sec                                               | 2.93 sec: 1.13x slower                                                       |
| hexiom                     | 6.16 ms                                                | 7.00 ms: 1.14x slower                                                        |
| sphinx                     | 1.03 sec                                               | 1.18 sec: 1.14x slower                                                       |
| async_tree_io_tg           | 857 ms                                                 | 986 ms: 1.15x slower                                                         |
| genshi_xml                 | 50.9 ms                                                | 58.8 ms: 1.15x slower                                                        |
| sympy_sum                  | 150 ms                                                 | 175 ms: 1.17x slower                                                         |
| sympy_integrate            | 19.9 ms                                                | 23.4 ms: 1.18x slower                                                        |
| pylint                     | 313 ms                                                 | 376 ms: 1.20x slower                                                         |
| generators                 | 29.0 ms                                                | 35.9 ms: 1.24x slower                                                        |
| k_core                     | 2.35 sec                                               | 3.60 sec: 1.53x slower                                                       |
| bench_mp_pool              | 24.0 ms                                                | 84.3 ms: 3.51x slower                                                        |
| Geometric mean             | (ref)                                                  | 1.02x slower                                                                 |

Benchmark hidden because not significant (9): xml_etree_iterparse, coverage, coroutines, regex_dna, pycparser, asyncio_websockets, shortest_path, async_tree_none_tg, async_tree_cpu_io_mixed
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, mypy2, tornado_http
Ignored benchmarks (4) of results/bm-20241119-3.14.0a1+-735a0ce-JIT/bm-20241119-linux-x86_64-brandtbucher-justin_reserved_fram-3.14.0a1+-735a0ce.json: djangocms, many_optionals, sqlite_synth, subparsers

- Geometric mean (including insignificant results): 1.004x slower
# HPT report

- Reliability score: 94.22% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.07x