# Results vs. 3.13.0

- fork: python
- ref: 05a370abd6cdfe4b54be
- machine: linux-x86_64
- commit hash: 05a370a
- commit date: 2023-12-01
- overall geometric mean: 1.050x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231201-linux-x86_64-python-05a370abd6cdfe4b54be-3.13.0a2+-05a370a |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| chameleon      | 6.81 ms                                                | 6.94 ms: 1.02x slower                                                  |
| docutils       | 2.58 sec                                               | 2.61 sec: 1.01x slower                                                 |
| html5lib       | 63.4 ms                                                | 65.1 ms: 1.03x slower                                                  |
| sphinx         | 1.03 sec                                               | 1.07 sec: 1.03x slower                                                 |
| tornado_http   | 91.2 ms                                                | 95.9 ms: 1.05x slower                                                  |
| Geometric mean | (ref)                                                  | 1.02x slower                                                           |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231201-linux-x86_64-python-05a370abd6cdfe4b54be-3.13.0a2+-05a370a |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| coroutines                 | 22.2 ms                                                | 22.1 ms: 1.00x faster                                                  |
| asyncio_websockets         | 551 ms                                                 | 556 ms: 1.01x slower                                                   |
| async_generators           | 433 ms                                                 | 451 ms: 1.04x slower                                                   |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 740 ms: 1.29x slower                                                   |
| async_tree_memoization     | 437 ms                                                 | 571 ms: 1.31x slower                                                   |
| async_tree_none            | 350 ms                                                 | 472 ms: 1.35x slower                                                   |
| async_tree_memoization_tg  | 463 ms                                                 | 631 ms: 1.36x slower                                                   |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 746 ms: 1.37x slower                                                   |
| async_tree_io              | 838 ms                                                 | 1.20 sec: 1.43x slower                                                 |
| async_tree_io_tg           | 861 ms                                                 | 1.23 sec: 1.44x slower                                                 |
| async_tree_none_tg         | 319 ms                                                 | 461 ms: 1.44x slower                                                   |
| Geometric mean             | (ref)                                                  | 1.26x slower                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231201-linux-x86_64-python-05a370abd6cdfe4b54be-3.13.0a2+-05a370a |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pidigits       | 186 ms                                                 | 187 ms: 1.01x slower                                                   |
| float          | 78.7 ms                                                | 82.5 ms: 1.05x slower                                                  |
| nbody          | 87.7 ms                                                | 93.2 ms: 1.06x slower                                                  |
| Geometric mean | (ref)                                                  | 1.04x slower                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231201-linux-x86_64-python-05a370abd6cdfe4b54be-3.13.0a2+-05a370a |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_v8       | 26.9 ms                                                | 24.5 ms: 1.10x faster                                                  |
| regex_effbot   | 3.77 ms                                                | 3.58 ms: 1.05x faster                                                  |
| regex_dna      | 220 ms                                                 | 223 ms: 1.01x slower                                                   |
| regex_compile  | 132 ms                                                 | 135 ms: 1.02x slower                                                   |
| Geometric mean | (ref)                                                  | 1.03x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231201-linux-x86_64-python-05a370abd6cdfe4b54be-3.13.0a2+-05a370a |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| xml_etree_process    | 60.5 ms                                                | 59.9 ms: 1.01x faster                                                  |
| pickle_pure_python   | 302 us                                                 | 303 us: 1.00x slower                                                   |
| xml_etree_generate   | 86.8 ms                                                | 87.3 ms: 1.01x slower                                                  |
| xml_etree_parse      | 154 ms                                                 | 160 ms: 1.04x slower                                                   |
| json_dumps           | 10.1 ms                                                | 10.5 ms: 1.04x slower                                                  |
| unpickle_pure_python | 213 us                                                 | 221 us: 1.04x slower                                                   |
| json_loads           | 27.2 us                                                | 28.1 us: 1.04x slower                                                  |
| tomli_loads          | 2.12 sec                                               | 2.20 sec: 1.04x slower                                                 |
| xml_etree_iterparse  | 101 ms                                                 | 109 ms: 1.08x slower                                                   |
| Geometric mean       | (ref)                                                  | 1.03x slower                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231201-linux-x86_64-python-05a370abd6cdfe4b54be-3.13.0a2+-05a370a |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 12.6 ms: 1.00x faster                                                  |
| python_startup_no_site | 7.00 ms                                                | 9.03 ms: 1.29x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.13x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231201-linux-x86_64-python-05a370abd6cdfe4b54be-3.13.0a2+-05a370a |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_xml     | 50.5 ms                                                | 51.9 ms: 1.03x slower                                                  |
| genshi_text    | 22.6 ms                                                | 23.2 ms: 1.03x slower                                                  |
| mako           | 10.7 ms                                                | 11.1 ms: 1.04x slower                                                  |
| Geometric mean | (ref)                                                  | 1.02x slower                                                           |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231201-linux-x86_64-python-05a370abd6cdfe4b54be-3.13.0a2+-05a370a |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| typing_runtime_protocols   | 160 us                                                 | 115 us: 1.39x faster                                                   |
| regex_v8                   | 26.9 ms                                                | 24.5 ms: 1.10x faster                                                  |
| regex_effbot               | 3.77 ms                                                | 3.58 ms: 1.05x faster                                                  |
| crypto_pyaes               | 74.7 ms                                                | 71.3 ms: 1.05x faster                                                  |
| deepcopy_reduce            | 3.24 us                                                | 3.12 us: 1.04x faster                                                  |
| json                       | 5.32 ms                                                | 5.16 ms: 1.03x faster                                                  |
| sqlite_synth               | 2.90 us                                                | 2.82 us: 1.03x faster                                                  |
| sympy_sum                  | 150 ms                                                 | 147 ms: 1.03x faster                                                   |
| sympy_str                  | 273 ms                                                 | 266 ms: 1.03x faster                                                   |
| spectral_norm              | 113 ms                                                 | 111 ms: 1.02x faster                                                   |
| pyflate                    | 470 ms                                                 | 460 ms: 1.02x faster                                                   |
| sympy_integrate            | 19.8 ms                                                | 19.5 ms: 1.02x faster                                                  |
| sqlglot_normalize          | 108 ms                                                 | 106 ms: 1.02x faster                                                   |
| pycparser                  | 1.20 sec                                               | 1.18 sec: 1.02x faster                                                 |
| fannkuch                   | 394 ms                                                 | 388 ms: 1.02x faster                                                   |
| sympy_expand               | 456 ms                                                 | 450 ms: 1.01x faster                                                   |
| deepcopy                   | 354 us                                                 | 349 us: 1.01x faster                                                   |
| xml_etree_process          | 60.5 ms                                                | 59.9 ms: 1.01x faster                                                  |
| python_startup             | 12.7 ms                                                | 12.6 ms: 1.00x faster                                                  |
| coroutines                 | 22.2 ms                                                | 22.1 ms: 1.00x faster                                                  |
| sqlglot_optimize           | 53.4 ms                                                | 53.5 ms: 1.00x slower                                                  |
| pickle_pure_python         | 302 us                                                 | 303 us: 1.00x slower                                                   |
| pidigits                   | 186 ms                                                 | 187 ms: 1.01x slower                                                   |
| xml_etree_generate         | 86.8 ms                                                | 87.3 ms: 1.01x slower                                                  |
| nqueens                    | 80.9 ms                                                | 81.4 ms: 1.01x slower                                                  |
| go                         | 141 ms                                                 | 141 ms: 1.01x slower                                                   |
| telco                      | 8.40 ms                                                | 8.46 ms: 1.01x slower                                                  |
| create_gc_cycles           | 2.45 ms                                                | 2.47 ms: 1.01x slower                                                  |
| sqlglot_parse              | 1.26 ms                                                | 1.28 ms: 1.01x slower                                                  |
| deepcopy_memo              | 38.4 us                                                | 38.7 us: 1.01x slower                                                  |
| asyncio_websockets         | 551 ms                                                 | 556 ms: 1.01x slower                                                   |
| docutils                   | 2.58 sec                                               | 2.61 sec: 1.01x slower                                                 |
| meteor_contest             | 108 ms                                                 | 109 ms: 1.01x slower                                                   |
| connected_components       | 447 ms                                                 | 452 ms: 1.01x slower                                                   |
| pprint_safe_repr           | 727 ms                                                 | 735 ms: 1.01x slower                                                   |
| regex_dna                  | 220 ms                                                 | 223 ms: 1.01x slower                                                   |
| mdp                        | 2.54 sec                                               | 2.58 sec: 1.01x slower                                                 |
| richards_super             | 53.7 ms                                                | 54.4 ms: 1.01x slower                                                  |
| pprint_pformat             | 1.48 sec                                               | 1.50 sec: 1.02x slower                                                 |
| scimark_monte_carlo        | 66.8 ms                                                | 67.9 ms: 1.02x slower                                                  |
| sqlalchemy_imperative      | 16.9 ms                                                | 17.2 ms: 1.02x slower                                                  |
| sqlglot_transpile          | 1.57 ms                                                | 1.60 ms: 1.02x slower                                                  |
| chameleon                  | 6.81 ms                                                | 6.94 ms: 1.02x slower                                                  |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 5.13 ms: 1.02x slower                                                  |
| regex_compile              | 132 ms                                                 | 135 ms: 1.02x slower                                                   |
| hexiom                     | 6.08 ms                                                | 6.20 ms: 1.02x slower                                                  |
| logging_format             | 6.23 us                                                | 6.36 us: 1.02x slower                                                  |
| comprehensions             | 16.5 us                                                | 16.8 us: 1.02x slower                                                  |
| gc_traversal               | 4.90 ms                                                | 5.01 ms: 1.02x slower                                                  |
| richards                   | 47.5 ms                                                | 48.8 ms: 1.03x slower                                                  |
| many_optionals             | 857 us                                                 | 880 us: 1.03x slower                                                   |
| html5lib                   | 63.4 ms                                                | 65.1 ms: 1.03x slower                                                  |
| genshi_xml                 | 50.5 ms                                                | 51.9 ms: 1.03x slower                                                  |
| genshi_text                | 22.6 ms                                                | 23.2 ms: 1.03x slower                                                  |
| dulwich_log                | 64.6 ms                                                | 66.6 ms: 1.03x slower                                                  |
| deltablue                  | 3.19 ms                                                | 3.29 ms: 1.03x slower                                                  |
| logging_simple             | 5.65 us                                                | 5.83 us: 1.03x slower                                                  |
| sqlalchemy_declarative     | 133 ms                                                 | 137 ms: 1.03x slower                                                   |
| sphinx                     | 1.03 sec                                               | 1.07 sec: 1.03x slower                                                 |
| bench_thread_pool          | 818 us                                                 | 846 us: 1.03x slower                                                   |
| logging_silent             | 101 ns                                                 | 105 ns: 1.03x slower                                                   |
| xml_etree_parse            | 154 ms                                                 | 160 ms: 1.04x slower                                                   |
| json_dumps                 | 10.1 ms                                                | 10.5 ms: 1.04x slower                                                  |
| unpickle_pure_python       | 213 us                                                 | 221 us: 1.04x slower                                                   |
| generators                 | 28.8 ms                                                | 29.8 ms: 1.04x slower                                                  |
| json_loads                 | 27.2 us                                                | 28.1 us: 1.04x slower                                                  |
| tomli_loads                | 2.12 sec                                               | 2.20 sec: 1.04x slower                                                 |
| mako                       | 10.7 ms                                                | 11.1 ms: 1.04x slower                                                  |
| raytrace                   | 262 ms                                                 | 272 ms: 1.04x slower                                                   |
| async_generators           | 433 ms                                                 | 451 ms: 1.04x slower                                                   |
| chaos                      | 58.0 ms                                                | 60.7 ms: 1.05x slower                                                  |
| float                      | 78.7 ms                                                | 82.5 ms: 1.05x slower                                                  |
| tornado_http               | 91.2 ms                                                | 95.9 ms: 1.05x slower                                                  |
| gunicorn                   | 1.18 ms                                                | 1.25 ms: 1.05x slower                                                  |
| nbody                      | 87.7 ms                                                | 93.2 ms: 1.06x slower                                                  |
| pathlib                    | 17.4 ms                                                | 18.6 ms: 1.07x slower                                                  |
| bpe_tokeniser              | 4.69 sec                                               | 5.03 sec: 1.07x slower                                                 |
| xml_etree_iterparse        | 101 ms                                                 | 109 ms: 1.08x slower                                                   |
| k_core                     | 2.37 sec                                               | 2.67 sec: 1.13x slower                                                 |
| coverage                   | 82.8 ms                                                | 95.6 ms: 1.15x slower                                                  |
| python_startup_no_site     | 7.00 ms                                                | 9.03 ms: 1.29x slower                                                  |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 740 ms: 1.29x slower                                                   |
| async_tree_memoization     | 437 ms                                                 | 571 ms: 1.31x slower                                                   |
| async_tree_none            | 350 ms                                                 | 472 ms: 1.35x slower                                                   |
| async_tree_memoization_tg  | 463 ms                                                 | 631 ms: 1.36x slower                                                   |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 746 ms: 1.37x slower                                                   |
| async_tree_io              | 838 ms                                                 | 1.20 sec: 1.43x slower                                                 |
| async_tree_io_tg           | 861 ms                                                 | 1.23 sec: 1.44x slower                                                 |
| async_tree_none_tg         | 319 ms                                                 | 461 ms: 1.44x slower                                                   |
| subparsers                 | 15.5 ms                                                | 51.8 ms: 3.35x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.05x slower                                                           |

Benchmark hidden because not significant (9): pylint, scimark_lu, 2to3, scimark_sor, scimark_fft, django_template, bench_mp_pool, shortest_path, thrift
Ignored benchmarks (2) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: djangocms, gevent_hub

- Geometric mean (including insignificant results): 1.050x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x