# Results vs. 3.13.0

- fork: python
- ref: v3.14.0a1
- machine: linux-x86_64
- commit hash: 8cdaca8
- commit date: 2024-10-15
- overall geometric mean: 1.020x faster
- HPT reliability: 93.82%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241015-linux-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 254 ms: 1.05x faster                                       |
| docutils       | 2.59 sec                                               | 2.65 sec: 1.02x slower                                     |
| html5lib       | 64.2 ms                                                | 61.9 ms: 1.04x faster                                      |
| tornado_http   | 92.4 ms                                                | 89.9 ms: 1.03x faster                                      |
| Geometric mean | (ref)                                                  | 1.02x faster                                               |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241015-linux-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| async_tree_memoization_tg  | 464 ms                                                 | 376 ms: 1.23x faster                                       |
| async_tree_none            | 351 ms                                                 | 326 ms: 1.07x faster                                       |
| async_tree_memoization     | 442 ms                                                 | 415 ms: 1.07x faster                                       |
| asyncio_websockets         | 552 ms                                                 | 554 ms: 1.00x slower                                       |
| coroutines                 | 22.7 ms                                                | 23.1 ms: 1.02x slower                                      |
| async_generators           | 436 ms                                                 | 447 ms: 1.03x slower                                       |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 562 ms: 1.03x slower                                       |
| async_tree_io_tg           | 857 ms                                                 | 968 ms: 1.13x slower                                       |
| Geometric mean             | (ref)                                                  | 1.01x faster                                               |

Benchmark hidden because not significant (3): async_tree_cpu_io_mixed, async_tree_none_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241015-linux-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| pidigits       | 186 ms                                                 | 188 ms: 1.01x slower                                       |
| nbody          | 87.0 ms                                                | 88.8 ms: 1.02x slower                                      |
| Geometric mean | (ref)                                                  | 1.01x slower                                               |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241015-linux-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_effbot   | 3.73 ms                                                | 3.60 ms: 1.04x faster                                      |
| regex_v8       | 26.2 ms                                                | 25.5 ms: 1.03x faster                                      |
| regex_compile  | 132 ms                                                 | 129 ms: 1.02x faster                                       |
| regex_dna      | 218 ms                                                 | 214 ms: 1.02x faster                                       |
| Geometric mean | (ref)                                                  | 1.03x faster                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241015-linux-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| tomli_loads          | 2.14 sec                                               | 2.09 sec: 1.02x faster                                     |
| json_loads           | 27.2 us                                                | 26.9 us: 1.01x faster                                      |
| unpickle_pure_python | 216 us                                                 | 216 us: 1.00x slower                                       |
| pickle_pure_python   | 310 us                                                 | 313 us: 1.01x slower                                       |
| xml_etree_generate   | 86.7 ms                                                | 87.5 ms: 1.01x slower                                      |
| xml_etree_iterparse  | 101 ms                                                 | 104 ms: 1.03x slower                                       |
| json_dumps           | 10.6 ms                                                | 11.1 ms: 1.05x slower                                      |
| Geometric mean       | (ref)                                                  | 1.01x slower                                               |

Benchmark hidden because not significant (2): xml_etree_process, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241015-linux-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 12.5 ms                                                | 11.8 ms: 1.06x faster                                      |
| python_startup_no_site | 6.96 ms                                                | 7.02 ms: 1.01x slower                                      |
| Geometric mean         | (ref)                                                  | 1.02x faster                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241015-linux-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| django_template | 35.2 ms                                                | 34.0 ms: 1.03x faster                                      |
| mako            | 11.1 ms                                                | 11.2 ms: 1.01x slower                                      |
| genshi_xml      | 50.9 ms                                                | 52.1 ms: 1.02x slower                                      |
| Geometric mean  | (ref)                                                  | 1.00x faster                                               |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241015-linux-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| deepcopy                   | 358 us                                                 | 264 us: 1.36x faster                                       |
| deepcopy_memo              | 39.1 us                                                | 30.4 us: 1.29x faster                                      |
| async_tree_memoization_tg  | 464 ms                                                 | 376 ms: 1.23x faster                                       |
| go                         | 144 ms                                                 | 120 ms: 1.20x faster                                       |
| deepcopy_reduce            | 3.20 us                                                | 2.69 us: 1.19x faster                                      |
| pathlib                    | 17.5 ms                                                | 16.1 ms: 1.09x faster                                      |
| async_tree_none            | 351 ms                                                 | 326 ms: 1.07x faster                                       |
| generators                 | 29.0 ms                                                | 27.0 ms: 1.07x faster                                      |
| telco                      | 8.54 ms                                                | 7.97 ms: 1.07x faster                                      |
| pycparser                  | 1.20 sec                                               | 1.12 sec: 1.07x faster                                     |
| json                       | 5.36 ms                                                | 5.03 ms: 1.07x faster                                      |
| async_tree_memoization     | 442 ms                                                 | 415 ms: 1.07x faster                                       |
| richards                   | 48.7 ms                                                | 46.0 ms: 1.06x faster                                      |
| python_startup             | 12.5 ms                                                | 11.8 ms: 1.06x faster                                      |
| scimark_sparse_mat_mult    | 5.04 ms                                                | 4.79 ms: 1.05x faster                                      |
| 2to3                       | 267 ms                                                 | 254 ms: 1.05x faster                                       |
| thrift                     | 809 us                                                 | 773 us: 1.05x faster                                       |
| crypto_pyaes               | 75.3 ms                                                | 72.1 ms: 1.04x faster                                      |
| logging_format             | 6.40 us                                                | 6.13 us: 1.04x faster                                      |
| richards_super             | 54.9 ms                                                | 52.8 ms: 1.04x faster                                      |
| logging_simple             | 5.72 us                                                | 5.52 us: 1.04x faster                                      |
| html5lib                   | 64.2 ms                                                | 61.9 ms: 1.04x faster                                      |
| regex_effbot               | 3.73 ms                                                | 3.60 ms: 1.04x faster                                      |
| django_template            | 35.2 ms                                                | 34.0 ms: 1.03x faster                                      |
| sympy_str                  | 275 ms                                                 | 266 ms: 1.03x faster                                       |
| sympy_sum                  | 150 ms                                                 | 146 ms: 1.03x faster                                       |
| sympy_expand               | 463 ms                                                 | 450 ms: 1.03x faster                                       |
| tornado_http               | 92.4 ms                                                | 89.9 ms: 1.03x faster                                      |
| regex_v8                   | 26.2 ms                                                | 25.5 ms: 1.03x faster                                      |
| tomli_loads                | 2.14 sec                                               | 2.09 sec: 1.02x faster                                     |
| regex_compile              | 132 ms                                                 | 129 ms: 1.02x faster                                       |
| typing_runtime_protocols   | 165 us                                                 | 161 us: 1.02x faster                                       |
| raytrace                   | 267 ms                                                 | 262 ms: 1.02x faster                                       |
| regex_dna                  | 218 ms                                                 | 214 ms: 1.02x faster                                       |
| mdp                        | 2.72 sec                                               | 2.67 sec: 1.02x faster                                     |
| logging_silent             | 102 ns                                                 | 100 ns: 1.02x faster                                       |
| meteor_contest             | 109 ms                                                 | 107 ms: 1.02x faster                                       |
| spectral_norm              | 115 ms                                                 | 114 ms: 1.01x faster                                       |
| dulwich_log                | 64.3 ms                                                | 63.5 ms: 1.01x faster                                      |
| sqlglot_normalize          | 108 ms                                                 | 106 ms: 1.01x faster                                       |
| json_loads                 | 27.2 us                                                | 26.9 us: 1.01x faster                                      |
| scimark_fft                | 364 ms                                                 | 360 ms: 1.01x faster                                       |
| sqlglot_optimize           | 53.7 ms                                                | 53.2 ms: 1.01x faster                                      |
| coverage                   | 84.0 ms                                                | 83.6 ms: 1.01x faster                                      |
| sympy_integrate            | 19.9 ms                                                | 19.8 ms: 1.00x faster                                      |
| unpickle_pure_python       | 216 us                                                 | 216 us: 1.00x slower                                       |
| sqlglot_transpile          | 1.58 ms                                                | 1.59 ms: 1.00x slower                                      |
| asyncio_websockets         | 552 ms                                                 | 554 ms: 1.00x slower                                       |
| hexiom                     | 6.16 ms                                                | 6.19 ms: 1.00x slower                                      |
| pidigits                   | 186 ms                                                 | 188 ms: 1.01x slower                                       |
| pickle_pure_python         | 310 us                                                 | 313 us: 1.01x slower                                       |
| pprint_safe_repr           | 728 ms                                                 | 734 ms: 1.01x slower                                       |
| python_startup_no_site     | 6.96 ms                                                | 7.02 ms: 1.01x slower                                      |
| xml_etree_generate         | 86.7 ms                                                | 87.5 ms: 1.01x slower                                      |
| pprint_pformat             | 1.49 sec                                               | 1.51 sec: 1.01x slower                                     |
| comprehensions             | 16.5 us                                                | 16.7 us: 1.01x slower                                      |
| bpe_tokeniser              | 4.75 sec                                               | 4.80 sec: 1.01x slower                                     |
| sqlglot_parse              | 1.27 ms                                                | 1.29 ms: 1.01x slower                                      |
| mako                       | 11.1 ms                                                | 11.2 ms: 1.01x slower                                      |
| scimark_sor                | 124 ms                                                 | 125 ms: 1.02x slower                                       |
| coroutines                 | 22.7 ms                                                | 23.1 ms: 1.02x slower                                      |
| bench_thread_pool          | 822 us                                                 | 837 us: 1.02x slower                                       |
| nqueens                    | 78.4 ms                                                | 79.9 ms: 1.02x slower                                      |
| docutils                   | 2.59 sec                                               | 2.65 sec: 1.02x slower                                     |
| nbody                      | 87.0 ms                                                | 88.8 ms: 1.02x slower                                      |
| genshi_xml                 | 50.9 ms                                                | 52.1 ms: 1.02x slower                                      |
| async_generators           | 436 ms                                                 | 447 ms: 1.03x slower                                       |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 562 ms: 1.03x slower                                       |
| xml_etree_iterparse        | 101 ms                                                 | 104 ms: 1.03x slower                                       |
| chaos                      | 58.1 ms                                                | 60.1 ms: 1.03x slower                                      |
| gc_traversal               | 4.37 ms                                                | 4.54 ms: 1.04x slower                                      |
| json_dumps                 | 10.6 ms                                                | 11.1 ms: 1.05x slower                                      |
| create_gc_cycles           | 2.41 ms                                                | 2.67 ms: 1.11x slower                                      |
| async_tree_io_tg           | 857 ms                                                 | 968 ms: 1.13x slower                                       |
| bench_mp_pool              | 24.0 ms                                                | 77.9 ms: 3.25x slower                                      |
| Geometric mean             | (ref)                                                  | 1.01x faster                                               |

Benchmark hidden because not significant (14): async_tree_cpu_io_mixed, genshi_text, xml_etree_process, scimark_monte_carlo, pyflate, fannkuch, deltablue, float, async_tree_none_tg, scimark_lu, sphinx, xml_etree_parse, async_tree_io, pylint
Ignored benchmarks (8) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20241015-3.14.0a1-8cdaca8/bm-20241015-linux-x86_64-python-v3.14.0a1-3.14.0a1-8cdaca8.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.020x faster
# HPT report

- Reliability score: 93.82% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.02x