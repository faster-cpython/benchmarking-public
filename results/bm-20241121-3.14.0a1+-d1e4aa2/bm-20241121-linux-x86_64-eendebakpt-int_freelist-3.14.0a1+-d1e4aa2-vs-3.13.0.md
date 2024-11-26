# Results vs. 3.13.0

- fork: eendebakpt
- ref: int_freelist
- machine: linux-x86_64
- commit hash: d1e4aa2
- commit date: 2024-11-21
- overall geometric mean: 1.011x faster
- HPT reliability: 96.29%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241121-linux-x86_64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 257 ms: 1.04x faster                                               |
| docutils       | 2.59 sec                                               | 2.69 sec: 1.04x slower                                             |
| html5lib       | 64.2 ms                                                | 63.6 ms: 1.01x faster                                              |
| sphinx         | 1.03 sec                                               | 1.05 sec: 1.01x slower                                             |
| Geometric mean | (ref)                                                  | 1.00x slower                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241121-linux-x86_64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_memoization_tg  | 464 ms                                                 | 380 ms: 1.22x faster                                               |
| async_tree_none            | 351 ms                                                 | 327 ms: 1.07x faster                                               |
| async_tree_memoization     | 442 ms                                                 | 414 ms: 1.07x faster                                               |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 566 ms: 1.02x faster                                               |
| async_generators           | 436 ms                                                 | 432 ms: 1.01x faster                                               |
| asyncio_websockets         | 552 ms                                                 | 554 ms: 1.00x slower                                               |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 562 ms: 1.03x slower                                               |
| coroutines                 | 22.7 ms                                                | 23.9 ms: 1.05x slower                                              |
| async_tree_io_tg           | 857 ms                                                 | 979 ms: 1.14x slower                                               |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                       |

Benchmark hidden because not significant (2): async_tree_io, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241121-linux-x86_64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| pidigits       | 186 ms                                                 | 187 ms: 1.00x slower                                               |
| nbody          | 87.0 ms                                                | 94.4 ms: 1.09x slower                                              |
| Geometric mean | (ref)                                                  | 1.03x slower                                                       |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241121-linux-x86_64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                | 24.6 ms: 1.07x faster                                              |
| regex_effbot   | 3.73 ms                                                | 3.55 ms: 1.05x faster                                              |
| regex_compile  | 132 ms                                                 | 128 ms: 1.03x faster                                               |
| regex_dna      | 218 ms                                                 | 212 ms: 1.03x faster                                               |
| Geometric mean | (ref)                                                  | 1.05x faster                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241121-linux-x86_64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| tomli_loads          | 2.14 sec                                               | 2.02 sec: 1.06x faster                                             |
| xml_etree_process    | 60.6 ms                                                | 59.5 ms: 1.02x faster                                              |
| xml_etree_generate   | 86.7 ms                                                | 85.9 ms: 1.01x faster                                              |
| unpickle_pure_python | 216 us                                                 | 219 us: 1.01x slower                                               |
| xml_etree_parse      | 156 ms                                                 | 158 ms: 1.02x slower                                               |
| xml_etree_iterparse  | 101 ms                                                 | 106 ms: 1.05x slower                                               |
| pickle_pure_python   | 310 us                                                 | 327 us: 1.05x slower                                               |
| json_dumps           | 10.6 ms                                                | 11.4 ms: 1.08x slower                                              |
| Geometric mean       | (ref)                                                  | 1.01x slower                                                       |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241121-linux-x86_64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup_no_site | 6.96 ms                                                | 7.07 ms: 1.02x slower                                              |
| python_startup         | 12.5 ms                                                | 12.8 ms: 1.03x slower                                              |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241121-linux-x86_64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| django_template | 35.2 ms                                                | 32.0 ms: 1.10x faster                                              |
| genshi_text     | 23.5 ms                                                | 22.7 ms: 1.04x faster                                              |
| genshi_xml      | 50.9 ms                                                | 50.6 ms: 1.01x faster                                              |
| mako            | 11.1 ms                                                | 11.6 ms: 1.04x slower                                              |
| Geometric mean  | (ref)                                                  | 1.02x faster                                                       |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241121-linux-x86_64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| deepcopy                   | 358 us                                                 | 264 us: 1.36x faster                                               |
| deepcopy_memo              | 39.1 us                                                | 30.7 us: 1.27x faster                                              |
| async_tree_memoization_tg  | 464 ms                                                 | 380 ms: 1.22x faster                                               |
| go                         | 144 ms                                                 | 119 ms: 1.20x faster                                               |
| deepcopy_reduce            | 3.20 us                                                | 2.75 us: 1.16x faster                                              |
| spectral_norm              | 115 ms                                                 | 103 ms: 1.12x faster                                               |
| telco                      | 8.54 ms                                                | 7.77 ms: 1.10x faster                                              |
| django_template            | 35.2 ms                                                | 32.0 ms: 1.10x faster                                              |
| pathlib                    | 17.5 ms                                                | 16.0 ms: 1.09x faster                                              |
| scimark_sparse_mat_mult    | 5.04 ms                                                | 4.67 ms: 1.08x faster                                              |
| json                       | 5.36 ms                                                | 5.00 ms: 1.07x faster                                              |
| async_tree_none            | 351 ms                                                 | 327 ms: 1.07x faster                                               |
| async_tree_memoization     | 442 ms                                                 | 414 ms: 1.07x faster                                               |
| regex_v8                   | 26.2 ms                                                | 24.6 ms: 1.07x faster                                              |
| tomli_loads                | 2.14 sec                                               | 2.02 sec: 1.06x faster                                             |
| scimark_fft                | 364 ms                                                 | 345 ms: 1.06x faster                                               |
| regex_effbot               | 3.73 ms                                                | 3.55 ms: 1.05x faster                                              |
| crypto_pyaes               | 75.3 ms                                                | 71.7 ms: 1.05x faster                                              |
| richards_super             | 54.9 ms                                                | 52.7 ms: 1.04x faster                                              |
| thrift                     | 809 us                                                 | 778 us: 1.04x faster                                               |
| 2to3                       | 267 ms                                                 | 257 ms: 1.04x faster                                               |
| richards                   | 48.7 ms                                                | 46.9 ms: 1.04x faster                                              |
| generators                 | 29.0 ms                                                | 27.9 ms: 1.04x faster                                              |
| genshi_text                | 23.5 ms                                                | 22.7 ms: 1.04x faster                                              |
| sqlalchemy_declarative     | 133 ms                                                 | 129 ms: 1.04x faster                                               |
| logging_format             | 6.40 us                                                | 6.19 us: 1.03x faster                                              |
| pyflate                    | 471 ms                                                 | 456 ms: 1.03x faster                                               |
| regex_compile              | 132 ms                                                 | 128 ms: 1.03x faster                                               |
| regex_dna                  | 218 ms                                                 | 212 ms: 1.03x faster                                               |
| pycparser                  | 1.20 sec                                               | 1.18 sec: 1.02x faster                                             |
| sympy_sum                  | 150 ms                                                 | 148 ms: 1.02x faster                                               |
| xml_etree_process          | 60.6 ms                                                | 59.5 ms: 1.02x faster                                              |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 566 ms: 1.02x faster                                               |
| mdp                        | 2.72 sec                                               | 2.67 sec: 1.02x faster                                             |
| sympy_str                  | 275 ms                                                 | 271 ms: 1.02x faster                                               |
| scimark_sor                | 124 ms                                                 | 122 ms: 1.01x faster                                               |
| sympy_expand               | 463 ms                                                 | 457 ms: 1.01x faster                                               |
| typing_runtime_protocols   | 165 us                                                 | 163 us: 1.01x faster                                               |
| logging_simple             | 5.72 us                                                | 5.65 us: 1.01x faster                                              |
| meteor_contest             | 109 ms                                                 | 107 ms: 1.01x faster                                               |
| connected_components       | 444 ms                                                 | 439 ms: 1.01x faster                                               |
| xml_etree_generate         | 86.7 ms                                                | 85.9 ms: 1.01x faster                                              |
| html5lib                   | 64.2 ms                                                | 63.6 ms: 1.01x faster                                              |
| async_generators           | 436 ms                                                 | 432 ms: 1.01x faster                                               |
| genshi_xml                 | 50.9 ms                                                | 50.6 ms: 1.01x faster                                              |
| sqlglot_normalize          | 108 ms                                                 | 107 ms: 1.00x faster                                               |
| sqlglot_optimize           | 53.7 ms                                                | 53.6 ms: 1.00x faster                                              |
| asyncio_websockets         | 552 ms                                                 | 554 ms: 1.00x slower                                               |
| dulwich_log                | 64.3 ms                                                | 64.6 ms: 1.00x slower                                              |
| pidigits                   | 186 ms                                                 | 187 ms: 1.00x slower                                               |
| sqlglot_transpile          | 1.58 ms                                                | 1.59 ms: 1.00x slower                                              |
| pprint_safe_repr           | 728 ms                                                 | 734 ms: 1.01x slower                                               |
| pprint_pformat             | 1.49 sec                                               | 1.51 sec: 1.01x slower                                             |
| bpe_tokeniser              | 4.75 sec                                               | 4.80 sec: 1.01x slower                                             |
| sphinx                     | 1.03 sec                                               | 1.05 sec: 1.01x slower                                             |
| hexiom                     | 6.16 ms                                                | 6.25 ms: 1.01x slower                                              |
| unpickle_pure_python       | 216 us                                                 | 219 us: 1.01x slower                                               |
| xml_etree_parse            | 156 ms                                                 | 158 ms: 1.02x slower                                               |
| sqlglot_parse              | 1.27 ms                                                | 1.29 ms: 1.02x slower                                              |
| python_startup_no_site     | 6.96 ms                                                | 7.07 ms: 1.02x slower                                              |
| scimark_monte_carlo        | 67.4 ms                                                | 68.6 ms: 1.02x slower                                              |
| deltablue                  | 3.23 ms                                                | 3.29 ms: 1.02x slower                                              |
| python_startup             | 12.5 ms                                                | 12.8 ms: 1.03x slower                                              |
| raytrace                   | 267 ms                                                 | 275 ms: 1.03x slower                                               |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 562 ms: 1.03x slower                                               |
| comprehensions             | 16.5 us                                                | 17.1 us: 1.04x slower                                              |
| nqueens                    | 78.4 ms                                                | 81.3 ms: 1.04x slower                                              |
| scimark_lu                 | 113 ms                                                 | 117 ms: 1.04x slower                                               |
| docutils                   | 2.59 sec                                               | 2.69 sec: 1.04x slower                                             |
| bench_thread_pool          | 822 us                                                 | 856 us: 1.04x slower                                               |
| mako                       | 11.1 ms                                                | 11.6 ms: 1.04x slower                                              |
| xml_etree_iterparse        | 101 ms                                                 | 106 ms: 1.05x slower                                               |
| chaos                      | 58.1 ms                                                | 60.9 ms: 1.05x slower                                              |
| coroutines                 | 22.7 ms                                                | 23.9 ms: 1.05x slower                                              |
| pickle_pure_python         | 310 us                                                 | 327 us: 1.05x slower                                               |
| json_dumps                 | 10.6 ms                                                | 11.4 ms: 1.08x slower                                              |
| nbody                      | 87.0 ms                                                | 94.4 ms: 1.09x slower                                              |
| gc_traversal               | 4.37 ms                                                | 4.75 ms: 1.09x slower                                              |
| create_gc_cycles           | 2.41 ms                                                | 2.70 ms: 1.12x slower                                              |
| async_tree_io_tg           | 857 ms                                                 | 979 ms: 1.14x slower                                               |
| k_core                     | 2.35 sec                                               | 3.61 sec: 1.53x slower                                             |
| bench_mp_pool              | 24.0 ms                                                | 79.1 ms: 3.30x slower                                              |
| Geometric mean             | (ref)                                                  | 1.00x slower                                                       |

Benchmark hidden because not significant (11): json_loads, shortest_path, sqlalchemy_imperative, coverage, float, logging_silent, sympy_integrate, fannkuch, async_tree_io, async_tree_none_tg, pylint
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, mypy2, tornado_http
Ignored benchmarks (4) of results/bm-20241121-3.14.0a1+-d1e4aa2/bm-20241121-linux-x86_64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2.json: djangocms, many_optionals, sqlite_synth, subparsers

- Geometric mean (including insignificant results): 1.011x faster
# HPT report

- Reliability score: 96.29% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.02x