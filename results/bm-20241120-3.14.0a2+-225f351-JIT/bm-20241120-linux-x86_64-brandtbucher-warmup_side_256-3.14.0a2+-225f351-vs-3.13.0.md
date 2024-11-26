# Results vs. 3.13.0

- fork: brandtbucher
- ref: warmup_side_256
- machine: linux-x86_64
- commit hash: 225f351
- commit date: 2024-11-20
- overall geometric mean: 1.013x faster
- HPT reliability: 70.89%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241120-linux-x86_64-brandtbucher-warmup_side_256-3.14.0a2+-225f351 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 262 ms: 1.02x faster                                                    |
| docutils       | 2.59 sec                                               | 2.79 sec: 1.08x slower                                                  |
| html5lib       | 64.2 ms                                                | 67.6 ms: 1.05x slower                                                   |
| sphinx         | 1.03 sec                                               | 1.10 sec: 1.06x slower                                                  |
| Geometric mean | (ref)                                                  | 1.04x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241120-linux-x86_64-brandtbucher-warmup_side_256-3.14.0a2+-225f351 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 464 ms                                                 | 400 ms: 1.16x faster                                                    |
| async_tree_memoization     | 442 ms                                                 | 415 ms: 1.06x faster                                                    |
| async_tree_none            | 351 ms                                                 | 330 ms: 1.06x faster                                                    |
| asyncio_websockets         | 552 ms                                                 | 555 ms: 1.01x slower                                                    |
| coroutines                 | 22.7 ms                                                | 23.1 ms: 1.02x slower                                                   |
| async_generators           | 436 ms                                                 | 453 ms: 1.04x slower                                                    |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 567 ms: 1.04x slower                                                    |
| async_tree_io_tg           | 857 ms                                                 | 922 ms: 1.08x slower                                                    |
| async_tree_io              | 842 ms                                                 | 922 ms: 1.10x slower                                                    |
| Geometric mean             | (ref)                                                  | 1.00x faster                                                            |

Benchmark hidden because not significant (2): async_tree_cpu_io_mixed, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241120-linux-x86_64-brandtbucher-warmup_side_256-3.14.0a2+-225f351 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 87.0 ms                                                | 83.1 ms: 1.05x faster                                                   |
| float          | 79.2 ms                                                | 78.4 ms: 1.01x faster                                                   |
| pidigits       | 186 ms                                                 | 187 ms: 1.00x slower                                                    |
| Geometric mean | (ref)                                                  | 1.02x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241120-linux-x86_64-brandtbucher-warmup_side_256-3.14.0a2+-225f351 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 3.73 ms                                                | 3.34 ms: 1.12x faster                                                   |
| regex_v8       | 26.2 ms                                                | 25.5 ms: 1.03x faster                                                   |
| regex_compile  | 132 ms                                                 | 131 ms: 1.01x faster                                                    |
| regex_dna      | 218 ms                                                 | 220 ms: 1.01x slower                                                    |
| Geometric mean | (ref)                                                  | 1.04x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241120-linux-x86_64-brandtbucher-warmup_side_256-3.14.0a2+-225f351 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| unpickle_pure_python | 216 us                                                 | 194 us: 1.11x faster                                                    |
| xml_etree_generate   | 86.7 ms                                                | 79.0 ms: 1.10x faster                                                   |
| tomli_loads          | 2.14 sec                                               | 1.96 sec: 1.09x faster                                                  |
| xml_etree_process    | 60.6 ms                                                | 55.5 ms: 1.09x faster                                                   |
| xml_etree_parse      | 156 ms                                                 | 148 ms: 1.05x faster                                                    |
| json_loads           | 27.2 us                                                | 26.4 us: 1.03x faster                                                   |
| xml_etree_iterparse  | 101 ms                                                 | 102 ms: 1.00x slower                                                    |
| pickle_pure_python   | 310 us                                                 | 321 us: 1.03x slower                                                    |
| json_dumps           | 10.6 ms                                                | 11.2 ms: 1.06x slower                                                   |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241120-linux-x86_64-brandtbucher-warmup_side_256-3.14.0a2+-225f351 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 6.96 ms                                                | 7.06 ms: 1.01x slower                                                   |
| python_startup         | 12.5 ms                                                | 12.9 ms: 1.03x slower                                                   |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241120-linux-x86_64-brandtbucher-warmup_side_256-3.14.0a2+-225f351 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 10.0 ms: 1.11x faster                                                   |
| django_template | 35.2 ms                                                | 33.2 ms: 1.06x faster                                                   |
| genshi_text     | 23.5 ms                                                | 25.5 ms: 1.08x slower                                                   |
| genshi_xml      | 50.9 ms                                                | 59.1 ms: 1.16x slower                                                   |
| Geometric mean  | (ref)                                                  | 1.02x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241120-linux-x86_64-brandtbucher-warmup_side_256-3.14.0a2+-225f351 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy                   | 358 us                                                 | 267 us: 1.34x faster                                                    |
| deepcopy_memo              | 39.1 us                                                | 29.6 us: 1.32x faster                                                   |
| richards                   | 48.7 ms                                                | 39.6 ms: 1.23x faster                                                   |
| deepcopy_reduce            | 3.20 us                                                | 2.66 us: 1.20x faster                                                   |
| richards_super             | 54.9 ms                                                | 46.7 ms: 1.17x faster                                                   |
| async_tree_memoization_tg  | 464 ms                                                 | 400 ms: 1.16x faster                                                    |
| scimark_fft                | 364 ms                                                 | 319 ms: 1.14x faster                                                    |
| telco                      | 8.54 ms                                                | 7.56 ms: 1.13x faster                                                   |
| pylint                     | 313 ms                                                 | 278 ms: 1.13x faster                                                    |
| json                       | 5.36 ms                                                | 4.80 ms: 1.12x faster                                                   |
| regex_effbot               | 3.73 ms                                                | 3.34 ms: 1.12x faster                                                   |
| unpickle_pure_python       | 216 us                                                 | 194 us: 1.11x faster                                                    |
| mako                       | 11.1 ms                                                | 10.0 ms: 1.11x faster                                                   |
| crypto_pyaes               | 75.3 ms                                                | 68.4 ms: 1.10x faster                                                   |
| xml_etree_generate         | 86.7 ms                                                | 79.0 ms: 1.10x faster                                                   |
| tomli_loads                | 2.14 sec                                               | 1.96 sec: 1.09x faster                                                  |
| xml_etree_process          | 60.6 ms                                                | 55.5 ms: 1.09x faster                                                   |
| scimark_sparse_mat_mult    | 5.04 ms                                                | 4.62 ms: 1.09x faster                                                   |
| pathlib                    | 17.5 ms                                                | 16.2 ms: 1.08x faster                                                   |
| go                         | 144 ms                                                 | 135 ms: 1.06x faster                                                    |
| async_tree_memoization     | 442 ms                                                 | 415 ms: 1.06x faster                                                    |
| async_tree_none            | 351 ms                                                 | 330 ms: 1.06x faster                                                    |
| pycparser                  | 1.20 sec                                               | 1.13 sec: 1.06x faster                                                  |
| django_template            | 35.2 ms                                                | 33.2 ms: 1.06x faster                                                   |
| bpe_tokeniser              | 4.75 sec                                               | 4.50 sec: 1.05x faster                                                  |
| logging_format             | 6.40 us                                                | 6.07 us: 1.05x faster                                                   |
| xml_etree_parse            | 156 ms                                                 | 148 ms: 1.05x faster                                                    |
| scimark_monte_carlo        | 67.4 ms                                                | 64.3 ms: 1.05x faster                                                   |
| nbody                      | 87.0 ms                                                | 83.1 ms: 1.05x faster                                                   |
| pyflate                    | 471 ms                                                 | 450 ms: 1.05x faster                                                    |
| logging_simple             | 5.72 us                                                | 5.49 us: 1.04x faster                                                   |
| thrift                     | 809 us                                                 | 782 us: 1.03x faster                                                    |
| pprint_pformat             | 1.49 sec                                               | 1.45 sec: 1.03x faster                                                  |
| json_loads                 | 27.2 us                                                | 26.4 us: 1.03x faster                                                   |
| regex_v8                   | 26.2 ms                                                | 25.5 ms: 1.03x faster                                                   |
| sqlalchemy_declarative     | 133 ms                                                 | 130 ms: 1.03x faster                                                    |
| scimark_sor                | 124 ms                                                 | 121 ms: 1.02x faster                                                    |
| fannkuch                   | 404 ms                                                 | 396 ms: 1.02x faster                                                    |
| connected_components       | 444 ms                                                 | 435 ms: 1.02x faster                                                    |
| 2to3                       | 267 ms                                                 | 262 ms: 1.02x faster                                                    |
| spectral_norm              | 115 ms                                                 | 113 ms: 1.02x faster                                                    |
| logging_silent             | 102 ns                                                 | 100 ns: 1.02x faster                                                    |
| pprint_safe_repr           | 728 ms                                                 | 718 ms: 1.01x faster                                                    |
| regex_compile              | 132 ms                                                 | 131 ms: 1.01x faster                                                    |
| deltablue                  | 3.23 ms                                                | 3.19 ms: 1.01x faster                                                   |
| float                      | 79.2 ms                                                | 78.4 ms: 1.01x faster                                                   |
| meteor_contest             | 109 ms                                                 | 108 ms: 1.01x faster                                                    |
| coverage                   | 84.0 ms                                                | 83.5 ms: 1.01x faster                                                   |
| gc_traversal               | 4.37 ms                                                | 4.36 ms: 1.00x faster                                                   |
| pidigits                   | 186 ms                                                 | 187 ms: 1.00x slower                                                    |
| xml_etree_iterparse        | 101 ms                                                 | 102 ms: 1.00x slower                                                    |
| asyncio_websockets         | 552 ms                                                 | 555 ms: 1.01x slower                                                    |
| regex_dna                  | 218 ms                                                 | 220 ms: 1.01x slower                                                    |
| python_startup_no_site     | 6.96 ms                                                | 7.06 ms: 1.01x slower                                                   |
| mdp                        | 2.72 sec                                               | 2.77 sec: 1.02x slower                                                  |
| coroutines                 | 22.7 ms                                                | 23.1 ms: 1.02x slower                                                   |
| sqlalchemy_imperative      | 17.1 ms                                                | 17.4 ms: 1.02x slower                                                   |
| scimark_lu                 | 113 ms                                                 | 115 ms: 1.02x slower                                                    |
| chaos                      | 58.1 ms                                                | 59.8 ms: 1.03x slower                                                   |
| python_startup             | 12.5 ms                                                | 12.9 ms: 1.03x slower                                                   |
| typing_runtime_protocols   | 165 us                                                 | 170 us: 1.03x slower                                                    |
| sqlglot_normalize          | 108 ms                                                 | 111 ms: 1.03x slower                                                    |
| pickle_pure_python         | 310 us                                                 | 321 us: 1.03x slower                                                    |
| sympy_str                  | 275 ms                                                 | 285 ms: 1.04x slower                                                    |
| async_generators           | 436 ms                                                 | 453 ms: 1.04x slower                                                    |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 567 ms: 1.04x slower                                                    |
| sqlglot_transpile          | 1.58 ms                                                | 1.65 ms: 1.04x slower                                                   |
| sqlglot_optimize           | 53.7 ms                                                | 55.9 ms: 1.04x slower                                                   |
| dulwich_log                | 64.3 ms                                                | 67.5 ms: 1.05x slower                                                   |
| sqlglot_parse              | 1.27 ms                                                | 1.34 ms: 1.05x slower                                                   |
| html5lib                   | 64.2 ms                                                | 67.6 ms: 1.05x slower                                                   |
| sympy_expand               | 463 ms                                                 | 488 ms: 1.05x slower                                                    |
| sympy_integrate            | 19.9 ms                                                | 21.0 ms: 1.06x slower                                                   |
| sympy_sum                  | 150 ms                                                 | 159 ms: 1.06x slower                                                    |
| json_dumps                 | 10.6 ms                                                | 11.2 ms: 1.06x slower                                                   |
| sphinx                     | 1.03 sec                                               | 1.10 sec: 1.06x slower                                                  |
| bench_thread_pool          | 822 us                                                 | 875 us: 1.07x slower                                                    |
| raytrace                   | 267 ms                                                 | 287 ms: 1.07x slower                                                    |
| docutils                   | 2.59 sec                                               | 2.79 sec: 1.08x slower                                                  |
| async_tree_io_tg           | 857 ms                                                 | 922 ms: 1.08x slower                                                    |
| genshi_text                | 23.5 ms                                                | 25.5 ms: 1.08x slower                                                   |
| comprehensions             | 16.5 us                                                | 17.9 us: 1.09x slower                                                   |
| async_tree_io              | 842 ms                                                 | 922 ms: 1.10x slower                                                    |
| create_gc_cycles           | 2.41 ms                                                | 2.65 ms: 1.10x slower                                                   |
| nqueens                    | 78.4 ms                                                | 90.1 ms: 1.15x slower                                                   |
| genshi_xml                 | 50.9 ms                                                | 59.1 ms: 1.16x slower                                                   |
| hexiom                     | 6.16 ms                                                | 7.16 ms: 1.16x slower                                                   |
| generators                 | 29.0 ms                                                | 35.8 ms: 1.23x slower                                                   |
| k_core                     | 2.35 sec                                               | 2.93 sec: 1.24x slower                                                  |
| bench_mp_pool              | 24.0 ms                                                | 79.0 ms: 3.29x slower                                                   |
| Geometric mean             | (ref)                                                  | 1.00x faster                                                            |

Benchmark hidden because not significant (3): async_tree_cpu_io_mixed, async_tree_none_tg, shortest_path
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, mypy2, tornado_http
Ignored benchmarks (4) of results/bm-20241120-3.14.0a2+-225f351-JIT/bm-20241120-linux-x86_64-brandtbucher-warmup_side_256-3.14.0a2+-225f351.json: djangocms, many_optionals, sqlite_synth, subparsers

- Geometric mean (including insignificant results): 1.013x faster
# HPT report

- Reliability score: 70.89% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.04x