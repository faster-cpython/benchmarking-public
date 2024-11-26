# Results vs. 3.13.0

- fork: faster-cpython
- ref: mark_first_2
- machine: linux-x86_64
- commit hash: 79ab26c
- commit date: 2024-11-22
- overall geometric mean: 1.042x faster
- HPT reliability: 99.98%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241122-linux-x86_64-faster%2dcpython-mark_first_2-3.14.0a2+-79ab26c |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 256 ms: 1.04x faster                                                     |
| docutils       | 2.59 sec                                               | 2.61 sec: 1.01x slower                                                   |
| html5lib       | 64.2 ms                                                | 62.7 ms: 1.02x faster                                                    |
| Geometric mean | (ref)                                                  | 1.02x faster                                                             |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241122-linux-x86_64-faster%2dcpython-mark_first_2-3.14.0a2+-79ab26c |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 464 ms                                                 | 316 ms: 1.47x faster                                                     |
| async_tree_io_tg           | 857 ms                                                 | 616 ms: 1.39x faster                                                     |
| async_tree_io              | 842 ms                                                 | 628 ms: 1.34x faster                                                     |
| async_tree_memoization     | 442 ms                                                 | 340 ms: 1.30x faster                                                     |
| async_tree_none            | 351 ms                                                 | 271 ms: 1.29x faster                                                     |
| async_tree_none_tg         | 321 ms                                                 | 254 ms: 1.26x faster                                                     |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 492 ms: 1.17x faster                                                     |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 479 ms: 1.14x faster                                                     |
| async_generators           | 436 ms                                                 | 427 ms: 1.02x faster                                                     |
| asyncio_websockets         | 552 ms                                                 | 555 ms: 1.01x slower                                                     |
| coroutines                 | 22.7 ms                                                | 23.9 ms: 1.05x slower                                                    |
| Geometric mean             | (ref)                                                  | 1.20x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241122-linux-x86_64-faster%2dcpython-mark_first_2-3.14.0a2+-79ab26c |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 79.2 ms                                                | 76.8 ms: 1.03x faster                                                    |
| pidigits       | 186 ms                                                 | 187 ms: 1.00x slower                                                     |
| nbody          | 87.0 ms                                                | 93.6 ms: 1.08x slower                                                    |
| Geometric mean | (ref)                                                  | 1.01x slower                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241122-linux-x86_64-faster%2dcpython-mark_first_2-3.14.0a2+-79ab26c |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 3.73 ms                                                | 3.55 ms: 1.05x faster                                                    |
| regex_compile  | 132 ms                                                 | 129 ms: 1.03x faster                                                     |
| regex_v8       | 26.2 ms                                                | 26.8 ms: 1.02x slower                                                    |
| regex_dna      | 218 ms                                                 | 226 ms: 1.04x slower                                                     |
| Geometric mean | (ref)                                                  | 1.00x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241122-linux-x86_64-faster%2dcpython-mark_first_2-3.14.0a2+-79ab26c |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_parse      | 156 ms                                                 | 139 ms: 1.12x faster                                                     |
| xml_etree_iterparse  | 101 ms                                                 | 97.7 ms: 1.04x faster                                                    |
| json_loads           | 27.2 us                                                | 26.6 us: 1.02x faster                                                    |
| tomli_loads          | 2.14 sec                                               | 2.10 sec: 1.02x faster                                                   |
| xml_etree_generate   | 86.7 ms                                                | 85.0 ms: 1.02x faster                                                    |
| xml_etree_process    | 60.6 ms                                                | 59.5 ms: 1.02x faster                                                    |
| unpickle_pure_python | 216 us                                                 | 218 us: 1.01x slower                                                     |
| pickle_pure_python   | 310 us                                                 | 319 us: 1.03x slower                                                     |
| json_dumps           | 10.6 ms                                                | 11.3 ms: 1.07x slower                                                    |
| Geometric mean       | (ref)                                                  | 1.01x faster                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241122-linux-x86_64-faster%2dcpython-mark_first_2-3.14.0a2+-79ab26c |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 6.96 ms                                                | 7.04 ms: 1.01x slower                                                    |
| python_startup         | 12.5 ms                                                | 12.7 ms: 1.02x slower                                                    |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241122-linux-x86_64-faster%2dcpython-mark_first_2-3.14.0a2+-79ab26c |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| django_template | 35.2 ms                                                | 32.0 ms: 1.10x faster                                                    |
| genshi_text     | 23.5 ms                                                | 22.4 ms: 1.05x faster                                                    |
| mako            | 11.1 ms                                                | 11.5 ms: 1.04x slower                                                    |
| Geometric mean  | (ref)                                                  | 1.03x faster                                                             |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241122-linux-x86_64-faster%2dcpython-mark_first_2-3.14.0a2+-79ab26c |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 464 ms                                                 | 316 ms: 1.47x faster                                                     |
| async_tree_io_tg           | 857 ms                                                 | 616 ms: 1.39x faster                                                     |
| deepcopy                   | 358 us                                                 | 259 us: 1.38x faster                                                     |
| async_tree_io              | 842 ms                                                 | 628 ms: 1.34x faster                                                     |
| async_tree_memoization     | 442 ms                                                 | 340 ms: 1.30x faster                                                     |
| async_tree_none            | 351 ms                                                 | 271 ms: 1.29x faster                                                     |
| deepcopy_memo              | 39.1 us                                                | 30.3 us: 1.29x faster                                                    |
| async_tree_none_tg         | 321 ms                                                 | 254 ms: 1.26x faster                                                     |
| go                         | 144 ms                                                 | 118 ms: 1.22x faster                                                     |
| deepcopy_reduce            | 3.20 us                                                | 2.67 us: 1.20x faster                                                    |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 492 ms: 1.17x faster                                                     |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 479 ms: 1.14x faster                                                     |
| pylint                     | 313 ms                                                 | 278 ms: 1.12x faster                                                     |
| xml_etree_parse            | 156 ms                                                 | 139 ms: 1.12x faster                                                     |
| django_template            | 35.2 ms                                                | 32.0 ms: 1.10x faster                                                    |
| telco                      | 8.54 ms                                                | 7.80 ms: 1.10x faster                                                    |
| pathlib                    | 17.5 ms                                                | 16.0 ms: 1.09x faster                                                    |
| json                       | 5.36 ms                                                | 4.99 ms: 1.07x faster                                                    |
| thrift                     | 809 us                                                 | 763 us: 1.06x faster                                                     |
| pycparser                  | 1.20 sec                                               | 1.14 sec: 1.06x faster                                                   |
| genshi_text                | 23.5 ms                                                | 22.4 ms: 1.05x faster                                                    |
| sqlalchemy_imperative      | 17.1 ms                                                | 16.2 ms: 1.05x faster                                                    |
| regex_effbot               | 3.73 ms                                                | 3.55 ms: 1.05x faster                                                    |
| sqlalchemy_declarative     | 133 ms                                                 | 127 ms: 1.05x faster                                                     |
| crypto_pyaes               | 75.3 ms                                                | 71.8 ms: 1.05x faster                                                    |
| richards                   | 48.7 ms                                                | 46.6 ms: 1.05x faster                                                    |
| logging_format             | 6.40 us                                                | 6.13 us: 1.04x faster                                                    |
| 2to3                       | 267 ms                                                 | 256 ms: 1.04x faster                                                     |
| richards_super             | 54.9 ms                                                | 52.6 ms: 1.04x faster                                                    |
| bpe_tokeniser              | 4.75 sec                                               | 4.58 sec: 1.04x faster                                                   |
| xml_etree_iterparse        | 101 ms                                                 | 97.7 ms: 1.04x faster                                                    |
| logging_simple             | 5.72 us                                                | 5.54 us: 1.03x faster                                                    |
| generators                 | 29.0 ms                                                | 28.1 ms: 1.03x faster                                                    |
| float                      | 79.2 ms                                                | 76.8 ms: 1.03x faster                                                    |
| mdp                        | 2.72 sec                                               | 2.64 sec: 1.03x faster                                                   |
| regex_compile              | 132 ms                                                 | 129 ms: 1.03x faster                                                     |
| k_core                     | 2.35 sec                                               | 2.29 sec: 1.03x faster                                                   |
| scimark_sparse_mat_mult    | 5.04 ms                                                | 4.92 ms: 1.02x faster                                                    |
| html5lib                   | 64.2 ms                                                | 62.7 ms: 1.02x faster                                                    |
| json_loads                 | 27.2 us                                                | 26.6 us: 1.02x faster                                                    |
| meteor_contest             | 109 ms                                                 | 107 ms: 1.02x faster                                                     |
| tomli_loads                | 2.14 sec                                               | 2.10 sec: 1.02x faster                                                   |
| xml_etree_generate         | 86.7 ms                                                | 85.0 ms: 1.02x faster                                                    |
| sympy_str                  | 275 ms                                                 | 269 ms: 1.02x faster                                                     |
| async_generators           | 436 ms                                                 | 427 ms: 1.02x faster                                                     |
| xml_etree_process          | 60.6 ms                                                | 59.5 ms: 1.02x faster                                                    |
| sympy_sum                  | 150 ms                                                 | 148 ms: 1.02x faster                                                     |
| pyflate                    | 471 ms                                                 | 465 ms: 1.01x faster                                                     |
| typing_runtime_protocols   | 165 us                                                 | 163 us: 1.01x faster                                                     |
| sympy_expand               | 463 ms                                                 | 460 ms: 1.01x faster                                                     |
| sympy_integrate            | 19.9 ms                                                | 19.9 ms: 1.00x faster                                                    |
| sqlglot_optimize           | 53.7 ms                                                | 53.6 ms: 1.00x faster                                                    |
| spectral_norm              | 115 ms                                                 | 115 ms: 1.00x faster                                                     |
| pidigits                   | 186 ms                                                 | 187 ms: 1.00x slower                                                     |
| docutils                   | 2.59 sec                                               | 2.61 sec: 1.01x slower                                                   |
| asyncio_websockets         | 552 ms                                                 | 555 ms: 1.01x slower                                                     |
| dulwich_log                | 64.3 ms                                                | 64.9 ms: 1.01x slower                                                    |
| hexiom                     | 6.16 ms                                                | 6.22 ms: 1.01x slower                                                    |
| unpickle_pure_python       | 216 us                                                 | 218 us: 1.01x slower                                                     |
| sqlglot_parse              | 1.27 ms                                                | 1.29 ms: 1.01x slower                                                    |
| pprint_pformat             | 1.49 sec                                               | 1.51 sec: 1.01x slower                                                   |
| sqlglot_transpile          | 1.58 ms                                                | 1.60 ms: 1.01x slower                                                    |
| python_startup_no_site     | 6.96 ms                                                | 7.04 ms: 1.01x slower                                                    |
| coverage                   | 84.0 ms                                                | 85.0 ms: 1.01x slower                                                    |
| scimark_fft                | 364 ms                                                 | 370 ms: 1.01x slower                                                     |
| raytrace                   | 267 ms                                                 | 272 ms: 1.02x slower                                                     |
| python_startup             | 12.5 ms                                                | 12.7 ms: 1.02x slower                                                    |
| comprehensions             | 16.5 us                                                | 16.8 us: 1.02x slower                                                    |
| regex_v8                   | 26.2 ms                                                | 26.8 ms: 1.02x slower                                                    |
| nqueens                    | 78.4 ms                                                | 80.2 ms: 1.02x slower                                                    |
| pprint_safe_repr           | 728 ms                                                 | 745 ms: 1.02x slower                                                     |
| scimark_monte_carlo        | 67.4 ms                                                | 69.1 ms: 1.02x slower                                                    |
| pickle_pure_python         | 310 us                                                 | 319 us: 1.03x slower                                                     |
| create_gc_cycles           | 2.41 ms                                                | 2.48 ms: 1.03x slower                                                    |
| scimark_sor                | 124 ms                                                 | 127 ms: 1.03x slower                                                     |
| scimark_lu                 | 113 ms                                                 | 116 ms: 1.03x slower                                                     |
| regex_dna                  | 218 ms                                                 | 226 ms: 1.04x slower                                                     |
| bench_thread_pool          | 822 us                                                 | 851 us: 1.04x slower                                                     |
| mako                       | 11.1 ms                                                | 11.5 ms: 1.04x slower                                                    |
| logging_silent             | 102 ns                                                 | 106 ns: 1.04x slower                                                     |
| chaos                      | 58.1 ms                                                | 60.8 ms: 1.05x slower                                                    |
| coroutines                 | 22.7 ms                                                | 23.9 ms: 1.05x slower                                                    |
| json_dumps                 | 10.6 ms                                                | 11.3 ms: 1.07x slower                                                    |
| nbody                      | 87.0 ms                                                | 93.6 ms: 1.08x slower                                                    |
| gc_traversal               | 4.37 ms                                                | 4.95 ms: 1.13x slower                                                    |
| bench_mp_pool              | 24.0 ms                                                | 80.8 ms: 3.37x slower                                                    |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                             |

Benchmark hidden because not significant (7): sphinx, fannkuch, connected_components, deltablue, shortest_path, sqlglot_normalize, genshi_xml
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, mypy2, tornado_http
Ignored benchmarks (4) of results/bm-20241122-3.14.0a2+-79ab26c/bm-20241122-linux-x86_64-faster%2dcpython-mark_first_2-3.14.0a2+-79ab26c.json: djangocms, many_optionals, sqlite_synth, subparsers

- Geometric mean (including insignificant results): 1.042x faster
# HPT report

- Reliability score: 99.98% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.02x