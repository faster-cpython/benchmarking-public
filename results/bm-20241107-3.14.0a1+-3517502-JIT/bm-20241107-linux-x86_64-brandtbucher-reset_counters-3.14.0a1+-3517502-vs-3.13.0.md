# Results vs. 3.13.0

- fork: brandtbucher
- ref: reset_counters
- machine: linux-x86_64
- commit hash: 3517502
- commit date: 2024-11-07
- overall geometric mean: 1.006x slower
- HPT reliability: 85.02%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241107-linux-x86_64-brandtbucher-reset_counters-3.14.0a1+-3517502 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 280 ms: 1.05x slower                                                   |
| docutils       | 2.59 sec                                               | 2.92 sec: 1.13x slower                                                 |
| html5lib       | 64.2 ms                                                | 65.4 ms: 1.02x slower                                                  |
| sphinx         | 1.03 sec                                               | 1.17 sec: 1.13x slower                                                 |
| Geometric mean | (ref)                                                  | 1.08x slower                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241107-linux-x86_64-brandtbucher-reset_counters-3.14.0a1+-3517502 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 464 ms                                                 | 381 ms: 1.22x faster                                                   |
| async_tree_memoization     | 442 ms                                                 | 414 ms: 1.07x faster                                                   |
| async_tree_none            | 351 ms                                                 | 331 ms: 1.06x faster                                                   |
| coroutines                 | 22.7 ms                                                | 22.4 ms: 1.01x faster                                                  |
| asyncio_websockets         | 552 ms                                                 | 558 ms: 1.01x slower                                                   |
| async_tree_io              | 842 ms                                                 | 859 ms: 1.02x slower                                                   |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 560 ms: 1.03x slower                                                   |
| async_generators           | 436 ms                                                 | 457 ms: 1.05x slower                                                   |
| async_tree_io_tg           | 857 ms                                                 | 971 ms: 1.13x slower                                                   |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                           |

Benchmark hidden because not significant (2): async_tree_cpu_io_mixed, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241107-linux-x86_64-brandtbucher-reset_counters-3.14.0a1+-3517502 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 87.0 ms                                                | 82.4 ms: 1.06x faster                                                  |
| float          | 79.2 ms                                                | 76.6 ms: 1.03x faster                                                  |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                                   |
| Geometric mean | (ref)                                                  | 1.03x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241107-linux-x86_64-brandtbucher-reset_counters-3.14.0a1+-3517502 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                | 24.5 ms: 1.07x faster                                                  |
| regex_effbot   | 3.73 ms                                                | 3.68 ms: 1.01x faster                                                  |
| regex_dna      | 218 ms                                                 | 216 ms: 1.01x faster                                                   |
| regex_compile  | 132 ms                                                 | 140 ms: 1.06x slower                                                   |
| Geometric mean | (ref)                                                  | 1.01x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241107-linux-x86_64-brandtbucher-reset_counters-3.14.0a1+-3517502 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 2.14 sec                                               | 1.94 sec: 1.10x faster                                                 |
| xml_etree_generate   | 86.7 ms                                                | 79.2 ms: 1.10x faster                                                  |
| xml_etree_process    | 60.6 ms                                                | 55.8 ms: 1.09x faster                                                  |
| xml_etree_parse      | 156 ms                                                 | 148 ms: 1.05x faster                                                   |
| json_loads           | 27.2 us                                                | 26.6 us: 1.02x faster                                                  |
| xml_etree_iterparse  | 101 ms                                                 | 101 ms: 1.01x faster                                                   |
| unpickle_pure_python | 216 us                                                 | 219 us: 1.02x slower                                                   |
| json_dumps           | 10.6 ms                                                | 11.0 ms: 1.04x slower                                                  |
| pickle_pure_python   | 310 us                                                 | 327 us: 1.05x slower                                                   |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241107-linux-x86_64-brandtbucher-reset_counters-3.14.0a1+-3517502 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 6.96 ms                                                | 7.12 ms: 1.02x slower                                                  |
| python_startup         | 12.5 ms                                                | 12.8 ms: 1.02x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241107-linux-x86_64-brandtbucher-reset_counters-3.14.0a1+-3517502 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 10.2 ms: 1.09x faster                                                  |
| django_template | 35.2 ms                                                | 36.1 ms: 1.03x slower                                                  |
| genshi_text     | 23.5 ms                                                | 25.9 ms: 1.10x slower                                                  |
| genshi_xml      | 50.9 ms                                                | 61.9 ms: 1.22x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.06x slower                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241107-linux-x86_64-brandtbucher-reset_counters-3.14.0a1+-3517502 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| deepcopy                   | 358 us                                                 | 267 us: 1.34x faster                                                   |
| deepcopy_memo              | 39.1 us                                                | 29.9 us: 1.31x faster                                                  |
| async_tree_memoization_tg  | 464 ms                                                 | 381 ms: 1.22x faster                                                   |
| deepcopy_reduce            | 3.20 us                                                | 2.70 us: 1.19x faster                                                  |
| richards                   | 48.7 ms                                                | 41.1 ms: 1.18x faster                                                  |
| scimark_fft                | 364 ms                                                 | 317 ms: 1.15x faster                                                   |
| richards_super             | 54.9 ms                                                | 48.2 ms: 1.14x faster                                                  |
| telco                      | 8.54 ms                                                | 7.60 ms: 1.12x faster                                                  |
| scimark_sparse_mat_mult    | 5.04 ms                                                | 4.51 ms: 1.12x faster                                                  |
| tomli_loads                | 2.14 sec                                               | 1.94 sec: 1.10x faster                                                 |
| crypto_pyaes               | 75.3 ms                                                | 68.6 ms: 1.10x faster                                                  |
| xml_etree_generate         | 86.7 ms                                                | 79.2 ms: 1.10x faster                                                  |
| mako                       | 11.1 ms                                                | 10.2 ms: 1.09x faster                                                  |
| pathlib                    | 17.5 ms                                                | 16.1 ms: 1.09x faster                                                  |
| xml_etree_process          | 60.6 ms                                                | 55.8 ms: 1.09x faster                                                  |
| go                         | 144 ms                                                 | 134 ms: 1.07x faster                                                   |
| regex_v8                   | 26.2 ms                                                | 24.5 ms: 1.07x faster                                                  |
| async_tree_memoization     | 442 ms                                                 | 414 ms: 1.07x faster                                                   |
| bpe_tokeniser              | 4.75 sec                                               | 4.47 sec: 1.06x faster                                                 |
| json                       | 5.36 ms                                                | 5.06 ms: 1.06x faster                                                  |
| async_tree_none            | 351 ms                                                 | 331 ms: 1.06x faster                                                   |
| nbody                      | 87.0 ms                                                | 82.4 ms: 1.06x faster                                                  |
| xml_etree_parse            | 156 ms                                                 | 148 ms: 1.05x faster                                                   |
| scimark_monte_carlo        | 67.4 ms                                                | 64.4 ms: 1.05x faster                                                  |
| pyflate                    | 471 ms                                                 | 451 ms: 1.04x faster                                                   |
| logging_format             | 6.40 us                                                | 6.13 us: 1.04x faster                                                  |
| fannkuch                   | 404 ms                                                 | 388 ms: 1.04x faster                                                   |
| pycparser                  | 1.20 sec                                               | 1.16 sec: 1.04x faster                                                 |
| thrift                     | 809 us                                                 | 782 us: 1.03x faster                                                   |
| float                      | 79.2 ms                                                | 76.6 ms: 1.03x faster                                                  |
| scimark_sor                | 124 ms                                                 | 120 ms: 1.03x faster                                                   |
| connected_components       | 444 ms                                                 | 432 ms: 1.03x faster                                                   |
| json_loads                 | 27.2 us                                                | 26.6 us: 1.02x faster                                                  |
| logging_simple             | 5.72 us                                                | 5.59 us: 1.02x faster                                                  |
| meteor_contest             | 109 ms                                                 | 107 ms: 1.01x faster                                                   |
| regex_effbot               | 3.73 ms                                                | 3.68 ms: 1.01x faster                                                  |
| regex_dna                  | 218 ms                                                 | 216 ms: 1.01x faster                                                   |
| logging_silent             | 102 ns                                                 | 100 ns: 1.01x faster                                                   |
| coroutines                 | 22.7 ms                                                | 22.4 ms: 1.01x faster                                                  |
| xml_etree_iterparse        | 101 ms                                                 | 101 ms: 1.01x faster                                                   |
| shortest_path              | 481 ms                                                 | 478 ms: 1.01x faster                                                   |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                                   |
| scimark_lu                 | 113 ms                                                 | 114 ms: 1.01x slower                                                   |
| asyncio_websockets         | 552 ms                                                 | 558 ms: 1.01x slower                                                   |
| mdp                        | 2.72 sec                                               | 2.76 sec: 1.02x slower                                                 |
| unpickle_pure_python       | 216 us                                                 | 219 us: 1.02x slower                                                   |
| html5lib                   | 64.2 ms                                                | 65.4 ms: 1.02x slower                                                  |
| coverage                   | 84.0 ms                                                | 85.7 ms: 1.02x slower                                                  |
| deltablue                  | 3.23 ms                                                | 3.29 ms: 1.02x slower                                                  |
| async_tree_io              | 842 ms                                                 | 859 ms: 1.02x slower                                                   |
| python_startup_no_site     | 6.96 ms                                                | 7.12 ms: 1.02x slower                                                  |
| python_startup             | 12.5 ms                                                | 12.8 ms: 1.02x slower                                                  |
| pprint_pformat             | 1.49 sec                                               | 1.53 sec: 1.02x slower                                                 |
| chaos                      | 58.1 ms                                                | 59.5 ms: 1.03x slower                                                  |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 560 ms: 1.03x slower                                                   |
| django_template            | 35.2 ms                                                | 36.1 ms: 1.03x slower                                                  |
| pprint_safe_repr           | 728 ms                                                 | 749 ms: 1.03x slower                                                   |
| typing_runtime_protocols   | 165 us                                                 | 170 us: 1.03x slower                                                   |
| comprehensions             | 16.5 us                                                | 17.1 us: 1.04x slower                                                  |
| json_dumps                 | 10.6 ms                                                | 11.0 ms: 1.04x slower                                                  |
| raytrace                   | 267 ms                                                 | 278 ms: 1.04x slower                                                   |
| sqlglot_parse              | 1.27 ms                                                | 1.33 ms: 1.04x slower                                                  |
| sqlalchemy_imperative      | 17.1 ms                                                | 17.8 ms: 1.04x slower                                                  |
| async_generators           | 436 ms                                                 | 457 ms: 1.05x slower                                                   |
| 2to3                       | 267 ms                                                 | 280 ms: 1.05x slower                                                   |
| dulwich_log                | 64.3 ms                                                | 67.7 ms: 1.05x slower                                                  |
| pickle_pure_python         | 310 us                                                 | 327 us: 1.05x slower                                                   |
| sqlglot_normalize          | 108 ms                                                 | 114 ms: 1.06x slower                                                   |
| regex_compile              | 132 ms                                                 | 140 ms: 1.06x slower                                                   |
| sqlglot_transpile          | 1.58 ms                                                | 1.69 ms: 1.07x slower                                                  |
| gc_traversal               | 4.37 ms                                                | 4.67 ms: 1.07x slower                                                  |
| bench_thread_pool          | 822 us                                                 | 891 us: 1.08x slower                                                   |
| sympy_expand               | 463 ms                                                 | 503 ms: 1.09x slower                                                   |
| sympy_str                  | 275 ms                                                 | 301 ms: 1.10x slower                                                   |
| genshi_text                | 23.5 ms                                                | 25.9 ms: 1.10x slower                                                  |
| sqlglot_optimize           | 53.7 ms                                                | 59.6 ms: 1.11x slower                                                  |
| sqlalchemy_declarative     | 133 ms                                                 | 148 ms: 1.11x slower                                                   |
| create_gc_cycles           | 2.41 ms                                                | 2.69 ms: 1.12x slower                                                  |
| nqueens                    | 78.4 ms                                                | 88.0 ms: 1.12x slower                                                  |
| sphinx                     | 1.03 sec                                               | 1.17 sec: 1.13x slower                                                 |
| docutils                   | 2.59 sec                                               | 2.92 sec: 1.13x slower                                                 |
| async_tree_io_tg           | 857 ms                                                 | 971 ms: 1.13x slower                                                   |
| hexiom                     | 6.16 ms                                                | 7.07 ms: 1.15x slower                                                  |
| sympy_sum                  | 150 ms                                                 | 174 ms: 1.15x slower                                                   |
| sympy_integrate            | 19.9 ms                                                | 23.3 ms: 1.17x slower                                                  |
| pylint                     | 313 ms                                                 | 378 ms: 1.21x slower                                                   |
| genshi_xml                 | 50.9 ms                                                | 61.9 ms: 1.22x slower                                                  |
| generators                 | 29.0 ms                                                | 35.9 ms: 1.24x slower                                                  |
| k_core                     | 2.35 sec                                               | 3.58 sec: 1.52x slower                                                 |
| bench_mp_pool              | 24.0 ms                                                | 84.6 ms: 3.53x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.02x slower                                                           |

Benchmark hidden because not significant (3): async_tree_cpu_io_mixed, spectral_norm, async_tree_none_tg
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, mypy2, tornado_http
Ignored benchmarks (1) of results/bm-20241107-3.14.0a1+-3517502-JIT/bm-20241107-linux-x86_64-brandtbucher-reset_counters-3.14.0a1+-3517502.json: sqlite_synth

- Geometric mean (including insignificant results): 1.006x slower
# HPT report

- Reliability score: 85.02% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.07x