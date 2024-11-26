# Results vs. 3.13.0

- fork: python
- ref: 6e06e01881dcffbeef5b
- machine: linux-x86_64
- commit hash: 6e06e01
- commit date: 2024-09-12
- overall geometric mean: 1.030x faster
- HPT reliability: 88.49%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.98x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 276 ms: 1.04x slower                                                  |
| docutils       | 2.59 sec                                               | 2.96 sec: 1.14x slower                                                |
| html5lib       | 64.2 ms                                                | 64.5 ms: 1.00x slower                                                 |
| tornado_http   | 92.4 ms                                                | 94.6 ms: 1.02x slower                                                 |
| Geometric mean | (ref)                                                  | 1.05x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg  | 464 ms                                                 | 388 ms: 1.19x faster                                                  |
| async_tree_memoization     | 442 ms                                                 | 401 ms: 1.10x faster                                                  |
| async_tree_none            | 351 ms                                                 | 321 ms: 1.09x faster                                                  |
| async_tree_none_tg         | 321 ms                                                 | 309 ms: 1.04x faster                                                  |
| asyncio_websockets         | 552 ms                                                 | 555 ms: 1.01x slower                                                  |
| coroutines                 | 22.7 ms                                                | 22.9 ms: 1.01x slower                                                 |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 555 ms: 1.02x slower                                                  |
| async_generators           | 436 ms                                                 | 461 ms: 1.06x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                          |

Benchmark hidden because not significant (3): async_tree_cpu_io_mixed, async_tree_io_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 79.2 ms                                                | 70.0 ms: 1.13x faster                                                 |
| nbody          | 87.0 ms                                                | 80.2 ms: 1.08x faster                                                 |
| pidigits       | 186 ms                                                 | 185 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                  | 1.07x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                | 24.7 ms: 1.06x faster                                                 |
| regex_dna      | 218 ms                                                 | 216 ms: 1.01x faster                                                  |
| regex_effbot   | 3.73 ms                                                | 3.80 ms: 1.02x slower                                                 |
| regex_compile  | 132 ms                                                 | 141 ms: 1.07x slower                                                  |
| Geometric mean | (ref)                                                  | 1.00x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|---------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads         | 2.14 sec                                               | 1.93 sec: 1.11x faster                                                |
| xml_etree_generate  | 86.7 ms                                                | 78.7 ms: 1.10x faster                                                 |
| xml_etree_process   | 60.6 ms                                                | 55.6 ms: 1.09x faster                                                 |
| xml_etree_parse     | 156 ms                                                 | 145 ms: 1.07x faster                                                  |
| json_dumps          | 10.6 ms                                                | 10.1 ms: 1.04x faster                                                 |
| xml_etree_iterparse | 101 ms                                                 | 97.9 ms: 1.03x faster                                                 |
| json_loads          | 27.2 us                                                | 26.7 us: 1.02x faster                                                 |
| pickle_pure_python  | 310 us                                                 | 305 us: 1.02x faster                                                  |
| Geometric mean      | (ref)                                                  | 1.05x faster                                                          |

Benchmark hidden because not significant (1): unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 12.5 ms                                                | 10.5 ms: 1.18x faster                                                 |
| python_startup_no_site | 6.96 ms                                                | 7.07 ms: 1.02x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.88 ms: 1.12x faster                                                 |
| django_template | 35.2 ms                                                | 35.3 ms: 1.01x slower                                                 |
| genshi_text     | 23.5 ms                                                | 25.4 ms: 1.08x slower                                                 |
| genshi_xml      | 50.9 ms                                                | 60.0 ms: 1.18x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.03x slower                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy_memo              | 39.1 us                                                | 27.2 us: 1.44x faster                                                 |
| deepcopy                   | 358 us                                                 | 258 us: 1.39x faster                                                  |
| create_gc_cycles           | 2.41 ms                                                | 1.74 ms: 1.39x faster                                                 |
| richards                   | 48.7 ms                                                | 39.9 ms: 1.22x faster                                                 |
| richards_super             | 54.9 ms                                                | 45.6 ms: 1.20x faster                                                 |
| scimark_sparse_mat_mult    | 5.04 ms                                                | 4.21 ms: 1.20x faster                                                 |
| deepcopy_reduce            | 3.20 us                                                | 2.68 us: 1.20x faster                                                 |
| async_tree_memoization_tg  | 464 ms                                                 | 388 ms: 1.19x faster                                                  |
| scimark_fft                | 364 ms                                                 | 308 ms: 1.18x faster                                                  |
| python_startup             | 12.5 ms                                                | 10.5 ms: 1.18x faster                                                 |
| spectral_norm              | 115 ms                                                 | 98.4 ms: 1.17x faster                                                 |
| crypto_pyaes               | 75.3 ms                                                | 65.8 ms: 1.14x faster                                                 |
| float                      | 79.2 ms                                                | 70.0 ms: 1.13x faster                                                 |
| mako                       | 11.1 ms                                                | 9.88 ms: 1.12x faster                                                 |
| tomli_loads                | 2.14 sec                                               | 1.93 sec: 1.11x faster                                                |
| gc_traversal               | 4.37 ms                                                | 3.94 ms: 1.11x faster                                                 |
| async_tree_memoization     | 442 ms                                                 | 401 ms: 1.10x faster                                                  |
| xml_etree_generate         | 86.7 ms                                                | 78.7 ms: 1.10x faster                                                 |
| pathlib                    | 17.5 ms                                                | 15.9 ms: 1.10x faster                                                 |
| go                         | 144 ms                                                 | 131 ms: 1.10x faster                                                  |
| async_tree_none            | 351 ms                                                 | 321 ms: 1.09x faster                                                  |
| xml_etree_process          | 60.6 ms                                                | 55.6 ms: 1.09x faster                                                 |
| nbody                      | 87.0 ms                                                | 80.2 ms: 1.08x faster                                                 |
| json                       | 5.36 ms                                                | 4.94 ms: 1.08x faster                                                 |
| fannkuch                   | 404 ms                                                 | 375 ms: 1.08x faster                                                  |
| xml_etree_parse            | 156 ms                                                 | 145 ms: 1.07x faster                                                  |
| scimark_monte_carlo        | 67.4 ms                                                | 63.0 ms: 1.07x faster                                                 |
| bpe_tokeniser              | 4.75 sec                                               | 4.44 sec: 1.07x faster                                                |
| telco                      | 8.54 ms                                                | 8.05 ms: 1.06x faster                                                 |
| regex_v8                   | 26.2 ms                                                | 24.7 ms: 1.06x faster                                                 |
| scimark_sor                | 124 ms                                                 | 117 ms: 1.05x faster                                                  |
| pyflate                    | 471 ms                                                 | 448 ms: 1.05x faster                                                  |
| json_dumps                 | 10.6 ms                                                | 10.1 ms: 1.04x faster                                                 |
| pycparser                  | 1.20 sec                                               | 1.15 sec: 1.04x faster                                                |
| async_tree_none_tg         | 321 ms                                                 | 309 ms: 1.04x faster                                                  |
| xml_etree_iterparse        | 101 ms                                                 | 97.9 ms: 1.03x faster                                                 |
| logging_format             | 6.40 us                                                | 6.24 us: 1.03x faster                                                 |
| mdp                        | 2.72 sec                                               | 2.66 sec: 1.02x faster                                                |
| thrift                     | 809 us                                                 | 790 us: 1.02x faster                                                  |
| scimark_lu                 | 113 ms                                                 | 110 ms: 1.02x faster                                                  |
| json_loads                 | 27.2 us                                                | 26.7 us: 1.02x faster                                                 |
| meteor_contest             | 109 ms                                                 | 107 ms: 1.02x faster                                                  |
| pickle_pure_python         | 310 us                                                 | 305 us: 1.02x faster                                                  |
| regex_dna                  | 218 ms                                                 | 216 ms: 1.01x faster                                                  |
| deltablue                  | 3.23 ms                                                | 3.21 ms: 1.01x faster                                                 |
| pidigits                   | 186 ms                                                 | 185 ms: 1.00x faster                                                  |
| html5lib                   | 64.2 ms                                                | 64.5 ms: 1.00x slower                                                 |
| django_template            | 35.2 ms                                                | 35.3 ms: 1.01x slower                                                 |
| asyncio_websockets         | 552 ms                                                 | 555 ms: 1.01x slower                                                  |
| coroutines                 | 22.7 ms                                                | 22.9 ms: 1.01x slower                                                 |
| comprehensions             | 16.5 us                                                | 16.6 us: 1.01x slower                                                 |
| coverage                   | 84.0 ms                                                | 85.2 ms: 1.01x slower                                                 |
| python_startup_no_site     | 6.96 ms                                                | 7.07 ms: 1.02x slower                                                 |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 555 ms: 1.02x slower                                                  |
| regex_effbot               | 3.73 ms                                                | 3.80 ms: 1.02x slower                                                 |
| bench_thread_pool          | 822 us                                                 | 839 us: 1.02x slower                                                  |
| logging_silent             | 102 ns                                                 | 104 ns: 1.02x slower                                                  |
| tornado_http               | 92.4 ms                                                | 94.6 ms: 1.02x slower                                                 |
| pprint_safe_repr           | 728 ms                                                 | 748 ms: 1.03x slower                                                  |
| 2to3                       | 267 ms                                                 | 276 ms: 1.04x slower                                                  |
| raytrace                   | 267 ms                                                 | 281 ms: 1.05x slower                                                  |
| sqlglot_normalize          | 108 ms                                                 | 113 ms: 1.05x slower                                                  |
| dulwich_log                | 64.3 ms                                                | 67.8 ms: 1.05x slower                                                 |
| async_generators           | 436 ms                                                 | 461 ms: 1.06x slower                                                  |
| sqlglot_parse              | 1.27 ms                                                | 1.35 ms: 1.06x slower                                                 |
| regex_compile              | 132 ms                                                 | 141 ms: 1.07x slower                                                  |
| sqlglot_transpile          | 1.58 ms                                                | 1.69 ms: 1.07x slower                                                 |
| pprint_pformat             | 1.49 sec                                               | 1.60 sec: 1.07x slower                                                |
| genshi_text                | 23.5 ms                                                | 25.4 ms: 1.08x slower                                                 |
| sqlglot_optimize           | 53.7 ms                                                | 58.2 ms: 1.08x slower                                                 |
| sympy_str                  | 275 ms                                                 | 299 ms: 1.09x slower                                                  |
| nqueens                    | 78.4 ms                                                | 85.5 ms: 1.09x slower                                                 |
| sympy_expand               | 463 ms                                                 | 506 ms: 1.09x slower                                                  |
| hexiom                     | 6.16 ms                                                | 6.86 ms: 1.11x slower                                                 |
| generators                 | 29.0 ms                                                | 32.8 ms: 1.13x slower                                                 |
| docutils                   | 2.59 sec                                               | 2.96 sec: 1.14x slower                                                |
| sympy_integrate            | 19.9 ms                                                | 22.8 ms: 1.15x slower                                                 |
| sympy_sum                  | 150 ms                                                 | 173 ms: 1.15x slower                                                  |
| genshi_xml                 | 50.9 ms                                                | 60.0 ms: 1.18x slower                                                 |
| pylint                     | 313 ms                                                 | 375 ms: 1.20x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                          |

Benchmark hidden because not significant (8): async_tree_cpu_io_mixed, chaos, bench_mp_pool, unpickle_pure_python, logging_simple, typing_runtime_protocols, async_tree_io_tg, async_tree_io
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20240912-3.14.0a0-6e06e01-JIT/bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.030x faster
# HPT report

- Reliability score: 88.49% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.98x