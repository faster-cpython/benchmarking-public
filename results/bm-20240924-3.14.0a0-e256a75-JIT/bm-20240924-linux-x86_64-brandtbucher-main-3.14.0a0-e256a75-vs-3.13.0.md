# Results vs. 3.13.0

- fork: brandtbucher
- ref: main
- machine: linux-x86_64
- commit hash: e256a75
- commit date: 2024-09-24
- overall geometric mean: 1.034x faster
- HPT reliability: 88.83%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.98x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-linux-x86_64-brandtbucher-main-3.14.0a0-e256a75 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 275 ms: 1.03x slower                                        |
| docutils       | 2.59 sec                                               | 2.95 sec: 1.14x slower                                      |
| html5lib       | 64.2 ms                                                | 64.7 ms: 1.01x slower                                       |
| tornado_http   | 92.4 ms                                                | 94.5 ms: 1.02x slower                                       |
| Geometric mean | (ref)                                                  | 1.05x slower                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-linux-x86_64-brandtbucher-main-3.14.0a0-e256a75 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------:|
| async_tree_memoization_tg  | 464 ms                                                 | 388 ms: 1.19x faster                                        |
| async_tree_none            | 351 ms                                                 | 317 ms: 1.11x faster                                        |
| async_tree_memoization     | 442 ms                                                 | 401 ms: 1.10x faster                                        |
| async_tree_none_tg         | 321 ms                                                 | 310 ms: 1.03x faster                                        |
| asyncio_websockets         | 552 ms                                                 | 555 ms: 1.01x slower                                        |
| coroutines                 | 22.7 ms                                                | 22.9 ms: 1.01x slower                                       |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 555 ms: 1.02x slower                                        |
| async_generators           | 436 ms                                                 | 450 ms: 1.03x slower                                        |
| async_tree_io              | 842 ms                                                 | 885 ms: 1.05x slower                                        |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                |

Benchmark hidden because not significant (2): async_tree_cpu_io_mixed, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-linux-x86_64-brandtbucher-main-3.14.0a0-e256a75 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------:|
| float          | 79.2 ms                                                | 69.2 ms: 1.14x faster                                       |
| nbody          | 87.0 ms                                                | 79.3 ms: 1.10x faster                                       |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                        |
| Geometric mean | (ref)                                                  | 1.08x faster                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-linux-x86_64-brandtbucher-main-3.14.0a0-e256a75 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                | 24.5 ms: 1.07x faster                                       |
| regex_effbot   | 3.73 ms                                                | 3.83 ms: 1.03x slower                                       |
| regex_dna      | 218 ms                                                 | 225 ms: 1.03x slower                                        |
| regex_compile  | 132 ms                                                 | 142 ms: 1.07x slower                                        |
| Geometric mean | (ref)                                                  | 1.01x slower                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-linux-x86_64-brandtbucher-main-3.14.0a0-e256a75 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------:|
| xml_etree_generate   | 86.7 ms                                                | 77.2 ms: 1.12x faster                                       |
| xml_etree_process    | 60.6 ms                                                | 54.7 ms: 1.11x faster                                       |
| tomli_loads          | 2.14 sec                                               | 1.94 sec: 1.10x faster                                      |
| xml_etree_parse      | 156 ms                                                 | 145 ms: 1.08x faster                                        |
| json_dumps           | 10.6 ms                                                | 10.2 ms: 1.04x faster                                       |
| xml_etree_iterparse  | 101 ms                                                 | 98.5 ms: 1.03x faster                                       |
| pickle_pure_python   | 310 us                                                 | 308 us: 1.01x faster                                        |
| json_loads           | 27.2 us                                                | 27.0 us: 1.01x faster                                       |
| unpickle_pure_python | 216 us                                                 | 215 us: 1.00x faster                                        |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-linux-x86_64-brandtbucher-main-3.14.0a0-e256a75 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------:|
| python_startup         | 12.5 ms                                                | 10.5 ms: 1.18x faster                                       |
| python_startup_no_site | 6.96 ms                                                | 7.06 ms: 1.01x slower                                       |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-linux-x86_64-brandtbucher-main-3.14.0a0-e256a75 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.80 ms: 1.13x faster                                       |
| django_template | 35.2 ms                                                | 36.0 ms: 1.02x slower                                       |
| genshi_text     | 23.5 ms                                                | 24.9 ms: 1.06x slower                                       |
| genshi_xml      | 50.9 ms                                                | 57.3 ms: 1.12x slower                                       |
| Geometric mean  | (ref)                                                  | 1.02x slower                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-linux-x86_64-brandtbucher-main-3.14.0a0-e256a75 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------:|
| deepcopy_memo              | 39.1 us                                                | 26.7 us: 1.47x faster                                       |
| create_gc_cycles           | 2.41 ms                                                | 1.74 ms: 1.39x faster                                       |
| deepcopy                   | 358 us                                                 | 260 us: 1.38x faster                                        |
| richards                   | 48.7 ms                                                | 39.4 ms: 1.24x faster                                       |
| richards_super             | 54.9 ms                                                | 45.2 ms: 1.21x faster                                       |
| deepcopy_reduce            | 3.20 us                                                | 2.64 us: 1.21x faster                                       |
| scimark_sparse_mat_mult    | 5.04 ms                                                | 4.16 ms: 1.21x faster                                       |
| async_tree_memoization_tg  | 464 ms                                                 | 388 ms: 1.19x faster                                        |
| python_startup             | 12.5 ms                                                | 10.5 ms: 1.18x faster                                       |
| gc_traversal               | 4.37 ms                                                | 3.70 ms: 1.18x faster                                       |
| scimark_fft                | 364 ms                                                 | 309 ms: 1.18x faster                                        |
| spectral_norm              | 115 ms                                                 | 100.0 ms: 1.15x faster                                      |
| float                      | 79.2 ms                                                | 69.2 ms: 1.14x faster                                       |
| crypto_pyaes               | 75.3 ms                                                | 66.4 ms: 1.13x faster                                       |
| mako                       | 11.1 ms                                                | 9.80 ms: 1.13x faster                                       |
| xml_etree_generate         | 86.7 ms                                                | 77.2 ms: 1.12x faster                                       |
| pathlib                    | 17.5 ms                                                | 15.8 ms: 1.11x faster                                       |
| xml_etree_process          | 60.6 ms                                                | 54.7 ms: 1.11x faster                                       |
| async_tree_none            | 351 ms                                                 | 317 ms: 1.11x faster                                        |
| tomli_loads                | 2.14 sec                                               | 1.94 sec: 1.10x faster                                      |
| async_tree_memoization     | 442 ms                                                 | 401 ms: 1.10x faster                                        |
| nbody                      | 87.0 ms                                                | 79.3 ms: 1.10x faster                                       |
| go                         | 144 ms                                                 | 131 ms: 1.09x faster                                        |
| scimark_monte_carlo        | 67.4 ms                                                | 61.9 ms: 1.09x faster                                       |
| fannkuch                   | 404 ms                                                 | 373 ms: 1.08x faster                                        |
| telco                      | 8.54 ms                                                | 7.93 ms: 1.08x faster                                       |
| xml_etree_parse            | 156 ms                                                 | 145 ms: 1.08x faster                                        |
| bpe_tokeniser              | 4.75 sec                                               | 4.42 sec: 1.07x faster                                      |
| regex_v8                   | 26.2 ms                                                | 24.5 ms: 1.07x faster                                       |
| json                       | 5.36 ms                                                | 5.03 ms: 1.07x faster                                       |
| mdp                        | 2.72 sec                                               | 2.55 sec: 1.07x faster                                      |
| scimark_sor                | 124 ms                                                 | 117 ms: 1.06x faster                                        |
| pyflate                    | 471 ms                                                 | 450 ms: 1.05x faster                                        |
| pycparser                  | 1.20 sec                                               | 1.15 sec: 1.04x faster                                      |
| json_dumps                 | 10.6 ms                                                | 10.2 ms: 1.04x faster                                       |
| thrift                     | 809 us                                                 | 782 us: 1.03x faster                                        |
| async_tree_none_tg         | 321 ms                                                 | 310 ms: 1.03x faster                                        |
| xml_etree_iterparse        | 101 ms                                                 | 98.5 ms: 1.03x faster                                       |
| logging_format             | 6.40 us                                                | 6.23 us: 1.03x faster                                       |
| typing_runtime_protocols   | 165 us                                                 | 161 us: 1.02x faster                                        |
| meteor_contest             | 109 ms                                                 | 107 ms: 1.02x faster                                        |
| scimark_lu                 | 113 ms                                                 | 111 ms: 1.01x faster                                        |
| pickle_pure_python         | 310 us                                                 | 308 us: 1.01x faster                                        |
| json_loads                 | 27.2 us                                                | 27.0 us: 1.01x faster                                       |
| deltablue                  | 3.23 ms                                                | 3.21 ms: 1.01x faster                                       |
| unpickle_pure_python       | 216 us                                                 | 215 us: 1.00x faster                                        |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                        |
| asyncio_websockets         | 552 ms                                                 | 555 ms: 1.01x slower                                        |
| html5lib                   | 64.2 ms                                                | 64.7 ms: 1.01x slower                                       |
| coroutines                 | 22.7 ms                                                | 22.9 ms: 1.01x slower                                       |
| logging_silent             | 102 ns                                                 | 103 ns: 1.01x slower                                        |
| python_startup_no_site     | 6.96 ms                                                | 7.06 ms: 1.01x slower                                       |
| bench_thread_pool          | 822 us                                                 | 835 us: 1.02x slower                                        |
| chaos                      | 58.1 ms                                                | 59.0 ms: 1.02x slower                                       |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 555 ms: 1.02x slower                                        |
| coverage                   | 84.0 ms                                                | 85.6 ms: 1.02x slower                                       |
| tornado_http               | 92.4 ms                                                | 94.5 ms: 1.02x slower                                       |
| django_template            | 35.2 ms                                                | 36.0 ms: 1.02x slower                                       |
| pprint_safe_repr           | 728 ms                                                 | 748 ms: 1.03x slower                                        |
| regex_effbot               | 3.73 ms                                                | 3.83 ms: 1.03x slower                                       |
| pprint_pformat             | 1.49 sec                                               | 1.54 sec: 1.03x slower                                      |
| regex_dna                  | 218 ms                                                 | 225 ms: 1.03x slower                                        |
| 2to3                       | 267 ms                                                 | 275 ms: 1.03x slower                                        |
| raytrace                   | 267 ms                                                 | 275 ms: 1.03x slower                                        |
| async_generators           | 436 ms                                                 | 450 ms: 1.03x slower                                        |
| sqlglot_parse              | 1.27 ms                                                | 1.34 ms: 1.05x slower                                       |
| dulwich_log                | 64.3 ms                                                | 67.7 ms: 1.05x slower                                       |
| async_tree_io              | 842 ms                                                 | 885 ms: 1.05x slower                                        |
| sqlglot_normalize          | 108 ms                                                 | 113 ms: 1.05x slower                                        |
| genshi_text                | 23.5 ms                                                | 24.9 ms: 1.06x slower                                       |
| sqlglot_transpile          | 1.58 ms                                                | 1.67 ms: 1.06x slower                                       |
| regex_compile              | 132 ms                                                 | 142 ms: 1.07x slower                                        |
| sqlglot_optimize           | 53.7 ms                                                | 58.0 ms: 1.08x slower                                       |
| sympy_expand               | 463 ms                                                 | 502 ms: 1.08x slower                                        |
| sympy_str                  | 275 ms                                                 | 298 ms: 1.09x slower                                        |
| nqueens                    | 78.4 ms                                                | 86.4 ms: 1.10x slower                                       |
| hexiom                     | 6.16 ms                                                | 6.86 ms: 1.11x slower                                       |
| genshi_xml                 | 50.9 ms                                                | 57.3 ms: 1.12x slower                                       |
| generators                 | 29.0 ms                                                | 32.8 ms: 1.13x slower                                       |
| docutils                   | 2.59 sec                                               | 2.95 sec: 1.14x slower                                      |
| sympy_sum                  | 150 ms                                                 | 172 ms: 1.14x slower                                        |
| sympy_integrate            | 19.9 ms                                                | 22.8 ms: 1.14x slower                                       |
| pylint                     | 313 ms                                                 | 371 ms: 1.19x slower                                        |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                |

Benchmark hidden because not significant (5): async_tree_cpu_io_mixed, logging_simple, comprehensions, bench_mp_pool, async_tree_io_tg
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20240924-3.14.0a0-e256a75-JIT/bm-20240924-linux-x86_64-brandtbucher-main-3.14.0a0-e256a75.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.034x faster
# HPT report

- Reliability score: 88.83% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.98x