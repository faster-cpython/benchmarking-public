# Results vs. 3.13.0

- fork: faster-cpython
- ref: eager_dict_tracking
- machine: linux-x86_64
- commit hash: 498979f
- commit date: 2024-11-19
- overall geometric mean: 1.014x faster
- HPT reliability: 89.05%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241119-linux-x86_64-faster%2dcpython-eager_dict_tracking-3.14.0a1+-498979f |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 257 ms: 1.04x faster                                                            |
| docutils       | 2.59 sec                                               | 2.67 sec: 1.03x slower                                                          |
| sphinx         | 1.03 sec                                               | 1.06 sec: 1.02x slower                                                          |
| Geometric mean | (ref)                                                  | 1.00x slower                                                                    |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241119-linux-x86_64-faster%2dcpython-eager_dict_tracking-3.14.0a1+-498979f |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 464 ms                                                 | 399 ms: 1.16x faster                                                            |
| async_tree_memoization     | 442 ms                                                 | 403 ms: 1.10x faster                                                            |
| async_tree_none            | 351 ms                                                 | 321 ms: 1.09x faster                                                            |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 559 ms: 1.03x faster                                                            |
| async_generators           | 436 ms                                                 | 430 ms: 1.01x faster                                                            |
| asyncio_websockets         | 552 ms                                                 | 556 ms: 1.01x slower                                                            |
| coroutines                 | 22.7 ms                                                | 23.3 ms: 1.03x slower                                                           |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 569 ms: 1.04x slower                                                            |
| async_tree_io_tg           | 857 ms                                                 | 915 ms: 1.07x slower                                                            |
| async_tree_io              | 842 ms                                                 | 906 ms: 1.08x slower                                                            |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                                    |

Benchmark hidden because not significant (1): async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241119-linux-x86_64-faster%2dcpython-eager_dict_tracking-3.14.0a1+-498979f |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 186 ms                                                 | 187 ms: 1.00x slower                                                            |
| float          | 79.2 ms                                                | 81.6 ms: 1.03x slower                                                           |
| nbody          | 87.0 ms                                                | 92.9 ms: 1.07x slower                                                           |
| Geometric mean | (ref)                                                  | 1.03x slower                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241119-linux-x86_64-faster%2dcpython-eager_dict_tracking-3.14.0a1+-498979f |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 3.73 ms                                                | 3.48 ms: 1.07x faster                                                           |
| regex_compile  | 132 ms                                                 | 129 ms: 1.03x faster                                                            |
| regex_v8       | 26.2 ms                                                | 26.3 ms: 1.00x slower                                                           |
| regex_dna      | 218 ms                                                 | 223 ms: 1.02x slower                                                            |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241119-linux-x86_64-faster%2dcpython-eager_dict_tracking-3.14.0a1+-498979f |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| xml_etree_parse      | 156 ms                                                 | 151 ms: 1.03x faster                                                            |
| json_loads           | 27.2 us                                                | 26.6 us: 1.02x faster                                                           |
| xml_etree_process    | 60.6 ms                                                | 59.9 ms: 1.01x faster                                                           |
| tomli_loads          | 2.14 sec                                               | 2.12 sec: 1.01x faster                                                          |
| xml_etree_generate   | 86.7 ms                                                | 86.0 ms: 1.01x faster                                                           |
| unpickle_pure_python | 216 us                                                 | 218 us: 1.01x slower                                                            |
| xml_etree_iterparse  | 101 ms                                                 | 105 ms: 1.04x slower                                                            |
| pickle_pure_python   | 310 us                                                 | 323 us: 1.04x slower                                                            |
| json_dumps           | 10.6 ms                                                | 11.4 ms: 1.08x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.01x slower                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241119-linux-x86_64-faster%2dcpython-eager_dict_tracking-3.14.0a1+-498979f |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 6.96 ms                                                | 7.05 ms: 1.01x slower                                                           |
| python_startup         | 12.5 ms                                                | 12.8 ms: 1.03x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241119-linux-x86_64-faster%2dcpython-eager_dict_tracking-3.14.0a1+-498979f |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| django_template | 35.2 ms                                                | 32.2 ms: 1.09x faster                                                           |
| genshi_text     | 23.5 ms                                                | 22.3 ms: 1.05x faster                                                           |
| genshi_xml      | 50.9 ms                                                | 49.9 ms: 1.02x faster                                                           |
| mako            | 11.1 ms                                                | 11.4 ms: 1.03x slower                                                           |
| Geometric mean  | (ref)                                                  | 1.03x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241119-linux-x86_64-faster%2dcpython-eager_dict_tracking-3.14.0a1+-498979f |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| deepcopy                   | 358 us                                                 | 259 us: 1.38x faster                                                            |
| deepcopy_memo              | 39.1 us                                                | 30.8 us: 1.27x faster                                                           |
| pylint                     | 313 ms                                                 | 262 ms: 1.19x faster                                                            |
| deepcopy_reduce            | 3.20 us                                                | 2.69 us: 1.19x faster                                                           |
| go                         | 144 ms                                                 | 123 ms: 1.17x faster                                                            |
| async_tree_memoization_tg  | 464 ms                                                 | 399 ms: 1.16x faster                                                            |
| pathlib                    | 17.5 ms                                                | 15.9 ms: 1.10x faster                                                           |
| async_tree_memoization     | 442 ms                                                 | 403 ms: 1.10x faster                                                            |
| async_tree_none            | 351 ms                                                 | 321 ms: 1.09x faster                                                            |
| django_template            | 35.2 ms                                                | 32.2 ms: 1.09x faster                                                           |
| json                       | 5.36 ms                                                | 4.96 ms: 1.08x faster                                                           |
| telco                      | 8.54 ms                                                | 7.94 ms: 1.08x faster                                                           |
| regex_effbot               | 3.73 ms                                                | 3.48 ms: 1.07x faster                                                           |
| scimark_sparse_mat_mult    | 5.04 ms                                                | 4.76 ms: 1.06x faster                                                           |
| genshi_text                | 23.5 ms                                                | 22.3 ms: 1.05x faster                                                           |
| pycparser                  | 1.20 sec                                               | 1.14 sec: 1.05x faster                                                          |
| thrift                     | 809 us                                                 | 770 us: 1.05x faster                                                            |
| generators                 | 29.0 ms                                                | 27.6 ms: 1.05x faster                                                           |
| sqlalchemy_declarative     | 133 ms                                                 | 128 ms: 1.04x faster                                                            |
| 2to3                       | 267 ms                                                 | 257 ms: 1.04x faster                                                            |
| logging_format             | 6.40 us                                                | 6.17 us: 1.04x faster                                                           |
| logging_simple             | 5.72 us                                                | 5.52 us: 1.04x faster                                                           |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 559 ms: 1.03x faster                                                            |
| xml_etree_parse            | 156 ms                                                 | 151 ms: 1.03x faster                                                            |
| sympy_str                  | 275 ms                                                 | 267 ms: 1.03x faster                                                            |
| regex_compile              | 132 ms                                                 | 129 ms: 1.03x faster                                                            |
| sympy_sum                  | 150 ms                                                 | 147 ms: 1.03x faster                                                            |
| crypto_pyaes               | 75.3 ms                                                | 73.6 ms: 1.02x faster                                                           |
| richards_super             | 54.9 ms                                                | 53.6 ms: 1.02x faster                                                           |
| richards                   | 48.7 ms                                                | 47.6 ms: 1.02x faster                                                           |
| json_loads                 | 27.2 us                                                | 26.6 us: 1.02x faster                                                           |
| genshi_xml                 | 50.9 ms                                                | 49.9 ms: 1.02x faster                                                           |
| meteor_contest             | 109 ms                                                 | 107 ms: 1.02x faster                                                            |
| mdp                        | 2.72 sec                                               | 2.68 sec: 1.01x faster                                                          |
| async_generators           | 436 ms                                                 | 430 ms: 1.01x faster                                                            |
| sympy_expand               | 463 ms                                                 | 457 ms: 1.01x faster                                                            |
| gc_traversal               | 4.37 ms                                                | 4.31 ms: 1.01x faster                                                           |
| xml_etree_process          | 60.6 ms                                                | 59.9 ms: 1.01x faster                                                           |
| sqlalchemy_imperative      | 17.1 ms                                                | 16.9 ms: 1.01x faster                                                           |
| shortest_path              | 481 ms                                                 | 476 ms: 1.01x faster                                                            |
| connected_components       | 444 ms                                                 | 440 ms: 1.01x faster                                                            |
| tomli_loads                | 2.14 sec                                               | 2.12 sec: 1.01x faster                                                          |
| xml_etree_generate         | 86.7 ms                                                | 86.0 ms: 1.01x faster                                                           |
| spectral_norm              | 115 ms                                                 | 114 ms: 1.01x faster                                                            |
| sqlglot_optimize           | 53.7 ms                                                | 53.3 ms: 1.01x faster                                                           |
| typing_runtime_protocols   | 165 us                                                 | 164 us: 1.01x faster                                                            |
| sqlglot_normalize          | 108 ms                                                 | 107 ms: 1.01x faster                                                            |
| pyflate                    | 471 ms                                                 | 469 ms: 1.00x faster                                                            |
| regex_v8                   | 26.2 ms                                                | 26.3 ms: 1.00x slower                                                           |
| pidigits                   | 186 ms                                                 | 187 ms: 1.00x slower                                                            |
| pprint_pformat             | 1.49 sec                                               | 1.50 sec: 1.01x slower                                                          |
| asyncio_websockets         | 552 ms                                                 | 556 ms: 1.01x slower                                                            |
| bpe_tokeniser              | 4.75 sec                                               | 4.78 sec: 1.01x slower                                                          |
| dulwich_log                | 64.3 ms                                                | 64.9 ms: 1.01x slower                                                           |
| hexiom                     | 6.16 ms                                                | 6.22 ms: 1.01x slower                                                           |
| unpickle_pure_python       | 216 us                                                 | 218 us: 1.01x slower                                                            |
| sqlglot_transpile          | 1.58 ms                                                | 1.60 ms: 1.01x slower                                                           |
| python_startup_no_site     | 6.96 ms                                                | 7.05 ms: 1.01x slower                                                           |
| coverage                   | 84.0 ms                                                | 85.5 ms: 1.02x slower                                                           |
| regex_dna                  | 218 ms                                                 | 223 ms: 1.02x slower                                                            |
| scimark_monte_carlo        | 67.4 ms                                                | 68.8 ms: 1.02x slower                                                           |
| sphinx                     | 1.03 sec                                               | 1.06 sec: 1.02x slower                                                          |
| nqueens                    | 78.4 ms                                                | 80.0 ms: 1.02x slower                                                           |
| scimark_lu                 | 113 ms                                                 | 116 ms: 1.03x slower                                                            |
| sqlglot_parse              | 1.27 ms                                                | 1.31 ms: 1.03x slower                                                           |
| raytrace                   | 267 ms                                                 | 274 ms: 1.03x slower                                                            |
| mako                       | 11.1 ms                                                | 11.4 ms: 1.03x slower                                                           |
| python_startup             | 12.5 ms                                                | 12.8 ms: 1.03x slower                                                           |
| docutils                   | 2.59 sec                                               | 2.67 sec: 1.03x slower                                                          |
| coroutines                 | 22.7 ms                                                | 23.3 ms: 1.03x slower                                                           |
| float                      | 79.2 ms                                                | 81.6 ms: 1.03x slower                                                           |
| comprehensions             | 16.5 us                                                | 17.0 us: 1.03x slower                                                           |
| bench_thread_pool          | 822 us                                                 | 851 us: 1.04x slower                                                            |
| xml_etree_iterparse        | 101 ms                                                 | 105 ms: 1.04x slower                                                            |
| pickle_pure_python         | 310 us                                                 | 323 us: 1.04x slower                                                            |
| scimark_sor                | 124 ms                                                 | 129 ms: 1.04x slower                                                            |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 569 ms: 1.04x slower                                                            |
| deltablue                  | 3.23 ms                                                | 3.38 ms: 1.05x slower                                                           |
| chaos                      | 58.1 ms                                                | 61.1 ms: 1.05x slower                                                           |
| nbody                      | 87.0 ms                                                | 92.9 ms: 1.07x slower                                                           |
| async_tree_io_tg           | 857 ms                                                 | 915 ms: 1.07x slower                                                            |
| async_tree_io              | 842 ms                                                 | 906 ms: 1.08x slower                                                            |
| logging_silent             | 102 ns                                                 | 110 ns: 1.08x slower                                                            |
| json_dumps                 | 10.6 ms                                                | 11.4 ms: 1.08x slower                                                           |
| create_gc_cycles           | 2.41 ms                                                | 2.64 ms: 1.10x slower                                                           |
| k_core                     | 2.35 sec                                               | 2.92 sec: 1.24x slower                                                          |
| bench_mp_pool              | 24.0 ms                                                | 78.5 ms: 3.27x slower                                                           |
| Geometric mean             | (ref)                                                  | 1.00x faster                                                                    |

Benchmark hidden because not significant (6): async_tree_none_tg, fannkuch, html5lib, sympy_integrate, scimark_fft, pprint_safe_repr
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, mypy2, tornado_http
Ignored benchmarks (4) of results/bm-20241119-3.14.0a1+-498979f/bm-20241119-linux-x86_64-faster%2dcpython-eager_dict_tracking-3.14.0a1+-498979f.json: djangocms, many_optionals, sqlite_synth, subparsers

- Geometric mean (including insignificant results): 1.014x faster
# HPT report

- Reliability score: 89.05% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.02x