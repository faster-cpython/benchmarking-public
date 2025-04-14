# Results vs. 3.13.0

- fork: iritkatriel
- ref: subscr_stats
- machine: linux-x86_64
- commit hash: 325408b
- commit date: 2025-04-03
- overall geometric mean: 1.051x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250403-linux-x86_64-iritkatriel-subscr_stats-3.14.0a6+-325408b |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 255 ms: 1.04x faster                                                |
| docutils       | 2.58 sec                                               | 2.59 sec: 1.00x slower                                              |
| html5lib       | 63.4 ms                                                | 62.8 ms: 1.01x faster                                               |
| sphinx         | 1.03 sec                                               | 1.01 sec: 1.02x faster                                              |
| Geometric mean | (ref)                                                  | 1.02x faster                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250403-linux-x86_64-iritkatriel-subscr_stats-3.14.0a6+-325408b |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 317 ms: 1.46x faster                                                |
| async_tree_io_tg           | 861 ms                                                 | 618 ms: 1.39x faster                                                |
| async_tree_memoization     | 437 ms                                                 | 314 ms: 1.39x faster                                                |
| async_tree_io              | 838 ms                                                 | 619 ms: 1.36x faster                                                |
| async_tree_none            | 350 ms                                                 | 262 ms: 1.34x faster                                                |
| async_tree_none_tg         | 319 ms                                                 | 254 ms: 1.26x faster                                                |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 487 ms: 1.18x faster                                                |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 476 ms: 1.14x faster                                                |
| async_generators           | 433 ms                                                 | 394 ms: 1.10x faster                                                |
| coroutines                 | 22.2 ms                                                | 23.8 ms: 1.07x slower                                               |
| Geometric mean             | (ref)                                                  | 1.22x faster                                                        |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250403-linux-x86_64-iritkatriel-subscr_stats-3.14.0a6+-325408b |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 71.4 ms: 1.10x faster                                               |
| pidigits       | 186 ms                                                 | 187 ms: 1.00x slower                                                |
| nbody          | 87.7 ms                                                | 97.0 ms: 1.11x slower                                               |
| Geometric mean | (ref)                                                  | 1.00x slower                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250403-linux-x86_64-iritkatriel-subscr_stats-3.14.0a6+-325408b |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_v8       | 26.9 ms                                                | 22.8 ms: 1.18x faster                                               |
| regex_dna      | 220 ms                                                 | 203 ms: 1.09x faster                                                |
| regex_compile  | 132 ms                                                 | 126 ms: 1.05x faster                                                |
| regex_effbot   | 3.77 ms                                                | 3.74 ms: 1.01x faster                                               |
| Geometric mean | (ref)                                                  | 1.08x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250403-linux-x86_64-iritkatriel-subscr_stats-3.14.0a6+-325408b |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| xml_etree_parse      | 154 ms                                                 | 141 ms: 1.09x faster                                                |
| tomli_loads          | 2.12 sec                                               | 1.96 sec: 1.08x faster                                              |
| xml_etree_iterparse  | 101 ms                                                 | 98.8 ms: 1.03x faster                                               |
| xml_etree_generate   | 86.8 ms                                                | 84.8 ms: 1.02x faster                                               |
| xml_etree_process    | 60.5 ms                                                | 59.5 ms: 1.02x faster                                               |
| unpickle_pure_python | 213 us                                                 | 219 us: 1.03x slower                                                |
| pickle_pure_python   | 302 us                                                 | 320 us: 1.06x slower                                                |
| json_loads           | 27.2 us                                                | 29.5 us: 1.09x slower                                               |
| json_dumps           | 10.1 ms                                                | 11.4 ms: 1.12x slower                                               |
| Geometric mean       | (ref)                                                  | 1.01x slower                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250403-linux-x86_64-iritkatriel-subscr_stats-3.14.0a6+-325408b |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 13.1 ms: 1.03x slower                                               |
| python_startup_no_site | 7.00 ms                                                | 8.16 ms: 1.17x slower                                               |
| Geometric mean         | (ref)                                                  | 1.10x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250403-linux-x86_64-iritkatriel-subscr_stats-3.14.0a6+-325408b |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.0 ms: 1.08x faster                                               |
| genshi_xml      | 50.5 ms                                                | 49.5 ms: 1.02x faster                                               |
| django_template | 31.7 ms                                                | 32.3 ms: 1.02x slower                                               |
| mako            | 10.7 ms                                                | 11.2 ms: 1.05x slower                                               |
| Geometric mean  | (ref)                                                  | 1.01x faster                                                        |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250403-linux-x86_64-iritkatriel-subscr_stats-3.14.0a6+-325408b |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                               | 1.23 sec: 2.07x faster                                              |
| async_tree_memoization_tg  | 463 ms                                                 | 317 ms: 1.46x faster                                                |
| async_tree_io_tg           | 861 ms                                                 | 618 ms: 1.39x faster                                                |
| async_tree_memoization     | 437 ms                                                 | 314 ms: 1.39x faster                                                |
| deepcopy                   | 354 us                                                 | 257 us: 1.38x faster                                                |
| async_tree_io              | 838 ms                                                 | 619 ms: 1.36x faster                                                |
| async_tree_none            | 350 ms                                                 | 262 ms: 1.34x faster                                                |
| deepcopy_memo              | 38.4 us                                                | 29.4 us: 1.30x faster                                               |
| async_tree_none_tg         | 319 ms                                                 | 254 ms: 1.26x faster                                                |
| go                         | 141 ms                                                 | 115 ms: 1.22x faster                                                |
| deepcopy_reduce            | 3.24 us                                                | 2.72 us: 1.19x faster                                               |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 487 ms: 1.18x faster                                                |
| regex_v8                   | 26.9 ms                                                | 22.8 ms: 1.18x faster                                               |
| spectral_norm              | 113 ms                                                 | 96.3 ms: 1.18x faster                                               |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 476 ms: 1.14x faster                                                |
| pylint                     | 312 ms                                                 | 276 ms: 1.13x faster                                                |
| dulwich_log                | 64.6 ms                                                | 58.3 ms: 1.11x faster                                               |
| float                      | 78.7 ms                                                | 71.4 ms: 1.10x faster                                               |
| async_generators           | 433 ms                                                 | 394 ms: 1.10x faster                                                |
| xml_etree_parse            | 154 ms                                                 | 141 ms: 1.09x faster                                                |
| regex_dna                  | 220 ms                                                 | 203 ms: 1.09x faster                                                |
| tomli_loads                | 2.12 sec                                               | 1.96 sec: 1.08x faster                                              |
| genshi_text                | 22.6 ms                                                | 21.0 ms: 1.08x faster                                               |
| telco                      | 8.40 ms                                                | 7.84 ms: 1.07x faster                                               |
| richards_super             | 53.7 ms                                                | 50.3 ms: 1.07x faster                                               |
| richards                   | 47.5 ms                                                | 44.6 ms: 1.07x faster                                               |
| pycparser                  | 1.20 sec                                               | 1.13 sec: 1.07x faster                                              |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.75 ms: 1.06x faster                                               |
| regex_compile              | 132 ms                                                 | 126 ms: 1.05x faster                                                |
| pathlib                    | 17.4 ms                                                | 16.6 ms: 1.05x faster                                               |
| scimark_fft                | 367 ms                                                 | 350 ms: 1.05x faster                                                |
| 2to3                       | 266 ms                                                 | 255 ms: 1.04x faster                                                |
| k_core                     | 2.37 sec                                               | 2.28 sec: 1.04x faster                                              |
| sqlite_synth               | 2.90 us                                                | 2.79 us: 1.04x faster                                               |
| sympy_integrate            | 19.8 ms                                                | 19.1 ms: 1.04x faster                                               |
| logging_simple             | 5.65 us                                                | 5.49 us: 1.03x faster                                               |
| logging_format             | 6.23 us                                                | 6.07 us: 1.03x faster                                               |
| xml_etree_iterparse        | 101 ms                                                 | 98.8 ms: 1.03x faster                                               |
| xml_etree_generate         | 86.8 ms                                                | 84.8 ms: 1.02x faster                                               |
| crypto_pyaes               | 74.7 ms                                                | 73.0 ms: 1.02x faster                                               |
| sqlalchemy_declarative     | 133 ms                                                 | 130 ms: 1.02x faster                                                |
| sphinx                     | 1.03 sec                                               | 1.01 sec: 1.02x faster                                              |
| sympy_str                  | 273 ms                                                 | 267 ms: 1.02x faster                                                |
| logging_silent             | 101 ns                                                 | 98.9 ns: 1.02x faster                                               |
| bpe_tokeniser              | 4.69 sec                                               | 4.59 sec: 1.02x faster                                              |
| sqlalchemy_imperative      | 16.9 ms                                                | 16.6 ms: 1.02x faster                                               |
| genshi_xml                 | 50.5 ms                                                | 49.5 ms: 1.02x faster                                               |
| xml_etree_process          | 60.5 ms                                                | 59.5 ms: 1.02x faster                                               |
| meteor_contest             | 108 ms                                                 | 107 ms: 1.02x faster                                                |
| sympy_sum                  | 150 ms                                                 | 148 ms: 1.02x faster                                                |
| scimark_sor                | 122 ms                                                 | 120 ms: 1.02x faster                                                |
| html5lib                   | 63.4 ms                                                | 62.8 ms: 1.01x faster                                               |
| generators                 | 28.8 ms                                                | 28.6 ms: 1.01x faster                                               |
| regex_effbot               | 3.77 ms                                                | 3.74 ms: 1.01x faster                                               |
| pidigits                   | 186 ms                                                 | 187 ms: 1.00x slower                                                |
| docutils                   | 2.58 sec                                               | 2.59 sec: 1.00x slower                                              |
| coverage                   | 82.8 ms                                                | 83.2 ms: 1.00x slower                                               |
| pyflate                    | 470 ms                                                 | 473 ms: 1.01x slower                                                |
| chaos                      | 58.0 ms                                                | 58.5 ms: 1.01x slower                                               |
| shortest_path              | 487 ms                                                 | 491 ms: 1.01x slower                                                |
| nqueens                    | 80.9 ms                                                | 81.7 ms: 1.01x slower                                               |
| create_gc_cycles           | 2.45 ms                                                | 2.48 ms: 1.01x slower                                               |
| raytrace                   | 262 ms                                                 | 265 ms: 1.01x slower                                                |
| scimark_monte_carlo        | 66.8 ms                                                | 68.0 ms: 1.02x slower                                               |
| django_template            | 31.7 ms                                                | 32.3 ms: 1.02x slower                                               |
| gc_traversal               | 4.90 ms                                                | 4.99 ms: 1.02x slower                                               |
| hexiom                     | 6.08 ms                                                | 6.23 ms: 1.02x slower                                               |
| unpickle_pure_python       | 213 us                                                 | 219 us: 1.03x slower                                                |
| comprehensions             | 16.5 us                                                | 17.0 us: 1.03x slower                                               |
| python_startup             | 12.7 ms                                                | 13.1 ms: 1.03x slower                                               |
| typing_runtime_protocols   | 160 us                                                 | 166 us: 1.03x slower                                                |
| mako                       | 10.7 ms                                                | 11.2 ms: 1.05x slower                                               |
| pickle_pure_python         | 302 us                                                 | 320 us: 1.06x slower                                                |
| bench_thread_pool          | 818 us                                                 | 871 us: 1.07x slower                                                |
| coroutines                 | 22.2 ms                                                | 23.8 ms: 1.07x slower                                               |
| json_loads                 | 27.2 us                                                | 29.5 us: 1.09x slower                                               |
| fannkuch                   | 394 ms                                                 | 429 ms: 1.09x slower                                                |
| many_optionals             | 857 us                                                 | 948 us: 1.11x slower                                                |
| nbody                      | 87.7 ms                                                | 97.0 ms: 1.11x slower                                               |
| json_dumps                 | 10.1 ms                                                | 11.4 ms: 1.12x slower                                               |
| python_startup_no_site     | 7.00 ms                                                | 8.16 ms: 1.17x slower                                               |
| subparsers                 | 15.5 ms                                                | 20.9 ms: 1.35x slower                                               |
| bench_mp_pool              | 24.0 ms                                                | 83.1 ms: 3.46x slower                                               |
| Geometric mean             | (ref)                                                  | 1.04x faster                                                        |

Benchmark hidden because not significant (8): json, scimark_lu, deltablue, sympy_expand, asyncio_websockets, pprint_pformat, connected_components, pprint_safe_repr
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (4) of results/bm-20250403-3.14.0a6+-325408b/bm-20250403-linux-x86_64-iritkatriel-subscr_stats-3.14.0a6+-325408b.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.051x faster

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.04x