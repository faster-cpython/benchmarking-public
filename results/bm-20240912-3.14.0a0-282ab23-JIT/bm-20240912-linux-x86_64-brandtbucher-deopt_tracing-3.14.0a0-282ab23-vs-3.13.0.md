# Results vs. 3.13.0

- fork: brandtbucher
- ref: deopt_tracing
- machine: linux-x86_64
- commit hash: 282ab23
- commit date: 2024-09-12
- overall geometric mean: 1.033x faster
- HPT reliability: 92.32%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.98x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-linux-x86_64-brandtbucher-deopt_tracing-3.14.0a0-282ab23 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 275 ms: 1.03x slower                                                 |
| docutils       | 2.59 sec                                               | 2.94 sec: 1.13x slower                                               |
| html5lib       | 64.2 ms                                                | 63.3 ms: 1.01x faster                                                |
| tornado_http   | 92.4 ms                                                | 94.7 ms: 1.02x slower                                                |
| Geometric mean | (ref)                                                  | 1.04x slower                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-linux-x86_64-brandtbucher-deopt_tracing-3.14.0a0-282ab23 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_memoization_tg  | 464 ms                                                 | 385 ms: 1.20x faster                                                 |
| async_tree_memoization     | 442 ms                                                 | 392 ms: 1.13x faster                                                 |
| async_tree_none            | 351 ms                                                 | 314 ms: 1.12x faster                                                 |
| async_tree_none_tg         | 321 ms                                                 | 305 ms: 1.05x faster                                                 |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 569 ms: 1.01x faster                                                 |
| asyncio_websockets         | 552 ms                                                 | 555 ms: 1.01x slower                                                 |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 553 ms: 1.01x slower                                                 |
| async_generators           | 436 ms                                                 | 458 ms: 1.05x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.04x faster                                                         |

Benchmark hidden because not significant (3): coroutines, async_tree_io, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-linux-x86_64-brandtbucher-deopt_tracing-3.14.0a0-282ab23 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| float          | 79.2 ms                                                | 70.0 ms: 1.13x faster                                                |
| nbody          | 87.0 ms                                                | 80.2 ms: 1.08x faster                                                |
| pidigits       | 186 ms                                                 | 185 ms: 1.01x faster                                                 |
| Geometric mean | (ref)                                                  | 1.07x faster                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-linux-x86_64-brandtbucher-deopt_tracing-3.14.0a0-282ab23 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                | 25.1 ms: 1.04x faster                                                |
| regex_effbot   | 3.73 ms                                                | 3.75 ms: 1.00x slower                                                |
| regex_dna      | 218 ms                                                 | 224 ms: 1.03x slower                                                 |
| regex_compile  | 132 ms                                                 | 140 ms: 1.06x slower                                                 |
| Geometric mean | (ref)                                                  | 1.01x slower                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-linux-x86_64-brandtbucher-deopt_tracing-3.14.0a0-282ab23 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| xml_etree_generate   | 86.7 ms                                                | 77.2 ms: 1.12x faster                                                |
| xml_etree_process    | 60.6 ms                                                | 54.2 ms: 1.12x faster                                                |
| tomli_loads          | 2.14 sec                                               | 1.97 sec: 1.09x faster                                               |
| xml_etree_parse      | 156 ms                                                 | 146 ms: 1.06x faster                                                 |
| json_dumps           | 10.6 ms                                                | 10.2 ms: 1.03x faster                                                |
| pickle_pure_python   | 310 us                                                 | 303 us: 1.02x faster                                                 |
| xml_etree_iterparse  | 101 ms                                                 | 98.8 ms: 1.02x faster                                                |
| unpickle_pure_python | 216 us                                                 | 215 us: 1.00x faster                                                 |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                         |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-linux-x86_64-brandtbucher-deopt_tracing-3.14.0a0-282ab23 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup         | 12.5 ms                                                | 10.6 ms: 1.18x faster                                                |
| python_startup_no_site | 6.96 ms                                                | 7.07 ms: 1.02x slower                                                |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-linux-x86_64-brandtbucher-deopt_tracing-3.14.0a0-282ab23 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.84 ms: 1.13x faster                                                |
| django_template | 35.2 ms                                                | 36.0 ms: 1.02x slower                                                |
| genshi_text     | 23.5 ms                                                | 25.2 ms: 1.07x slower                                                |
| genshi_xml      | 50.9 ms                                                | 59.8 ms: 1.17x slower                                                |
| Geometric mean  | (ref)                                                  | 1.03x slower                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-linux-x86_64-brandtbucher-deopt_tracing-3.14.0a0-282ab23 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| deepcopy_memo              | 39.1 us                                                | 26.8 us: 1.46x faster                                                |
| deepcopy                   | 358 us                                                 | 259 us: 1.38x faster                                                 |
| create_gc_cycles           | 2.41 ms                                                | 1.76 ms: 1.37x faster                                                |
| richards                   | 48.7 ms                                                | 39.9 ms: 1.22x faster                                                |
| deepcopy_reduce            | 3.20 us                                                | 2.66 us: 1.21x faster                                                |
| async_tree_memoization_tg  | 464 ms                                                 | 385 ms: 1.20x faster                                                 |
| richards_super             | 54.9 ms                                                | 45.7 ms: 1.20x faster                                                |
| python_startup             | 12.5 ms                                                | 10.6 ms: 1.18x faster                                                |
| scimark_fft                | 364 ms                                                 | 310 ms: 1.18x faster                                                 |
| scimark_sparse_mat_mult    | 5.04 ms                                                | 4.36 ms: 1.16x faster                                                |
| spectral_norm              | 115 ms                                                 | 100 ms: 1.15x faster                                                 |
| gc_traversal               | 4.37 ms                                                | 3.83 ms: 1.14x faster                                                |
| float                      | 79.2 ms                                                | 70.0 ms: 1.13x faster                                                |
| async_tree_memoization     | 442 ms                                                 | 392 ms: 1.13x faster                                                 |
| mako                       | 11.1 ms                                                | 9.84 ms: 1.13x faster                                                |
| crypto_pyaes               | 75.3 ms                                                | 67.0 ms: 1.12x faster                                                |
| xml_etree_generate         | 86.7 ms                                                | 77.2 ms: 1.12x faster                                                |
| xml_etree_process          | 60.6 ms                                                | 54.2 ms: 1.12x faster                                                |
| async_tree_none            | 351 ms                                                 | 314 ms: 1.12x faster                                                 |
| fannkuch                   | 404 ms                                                 | 371 ms: 1.09x faster                                                 |
| go                         | 144 ms                                                 | 132 ms: 1.09x faster                                                 |
| tomli_loads                | 2.14 sec                                               | 1.97 sec: 1.09x faster                                               |
| pathlib                    | 17.5 ms                                                | 16.1 ms: 1.09x faster                                                |
| nbody                      | 87.0 ms                                                | 80.2 ms: 1.08x faster                                                |
| telco                      | 8.54 ms                                                | 7.89 ms: 1.08x faster                                                |
| scimark_monte_carlo        | 67.4 ms                                                | 62.3 ms: 1.08x faster                                                |
| mdp                        | 2.72 sec                                               | 2.53 sec: 1.08x faster                                               |
| bpe_tokeniser              | 4.75 sec                                               | 4.45 sec: 1.07x faster                                               |
| xml_etree_parse            | 156 ms                                                 | 146 ms: 1.06x faster                                                 |
| scimark_sor                | 124 ms                                                 | 117 ms: 1.06x faster                                                 |
| async_tree_none_tg         | 321 ms                                                 | 305 ms: 1.05x faster                                                 |
| json                       | 5.36 ms                                                | 5.12 ms: 1.05x faster                                                |
| regex_v8                   | 26.2 ms                                                | 25.1 ms: 1.04x faster                                                |
| pyflate                    | 471 ms                                                 | 451 ms: 1.04x faster                                                 |
| thrift                     | 809 us                                                 | 778 us: 1.04x faster                                                 |
| json_dumps                 | 10.6 ms                                                | 10.2 ms: 1.03x faster                                                |
| meteor_contest             | 109 ms                                                 | 106 ms: 1.03x faster                                                 |
| logging_format             | 6.40 us                                                | 6.22 us: 1.03x faster                                                |
| pickle_pure_python         | 310 us                                                 | 303 us: 1.02x faster                                                 |
| xml_etree_iterparse        | 101 ms                                                 | 98.8 ms: 1.02x faster                                                |
| logging_simple             | 5.72 us                                                | 5.60 us: 1.02x faster                                                |
| typing_runtime_protocols   | 165 us                                                 | 162 us: 1.02x faster                                                 |
| scimark_lu                 | 113 ms                                                 | 111 ms: 1.02x faster                                                 |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 569 ms: 1.01x faster                                                 |
| html5lib                   | 64.2 ms                                                | 63.3 ms: 1.01x faster                                                |
| deltablue                  | 3.23 ms                                                | 3.19 ms: 1.01x faster                                                |
| pidigits                   | 186 ms                                                 | 185 ms: 1.01x faster                                                 |
| unpickle_pure_python       | 216 us                                                 | 215 us: 1.00x faster                                                 |
| regex_effbot               | 3.73 ms                                                | 3.75 ms: 1.00x slower                                                |
| comprehensions             | 16.5 us                                                | 16.6 us: 1.00x slower                                                |
| chaos                      | 58.1 ms                                                | 58.4 ms: 1.01x slower                                                |
| asyncio_websockets         | 552 ms                                                 | 555 ms: 1.01x slower                                                 |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 553 ms: 1.01x slower                                                 |
| python_startup_no_site     | 6.96 ms                                                | 7.07 ms: 1.02x slower                                                |
| bench_thread_pool          | 822 us                                                 | 835 us: 1.02x slower                                                 |
| logging_silent             | 102 ns                                                 | 104 ns: 1.02x slower                                                 |
| tornado_http               | 92.4 ms                                                | 94.7 ms: 1.02x slower                                                |
| django_template            | 35.2 ms                                                | 36.0 ms: 1.02x slower                                                |
| regex_dna                  | 218 ms                                                 | 224 ms: 1.03x slower                                                 |
| 2to3                       | 267 ms                                                 | 275 ms: 1.03x slower                                                 |
| raytrace                   | 267 ms                                                 | 277 ms: 1.04x slower                                                 |
| pprint_pformat             | 1.49 sec                                               | 1.56 sec: 1.04x slower                                               |
| sqlglot_parse              | 1.27 ms                                                | 1.34 ms: 1.05x slower                                                |
| async_generators           | 436 ms                                                 | 458 ms: 1.05x slower                                                 |
| dulwich_log                | 64.3 ms                                                | 67.7 ms: 1.05x slower                                                |
| regex_compile              | 132 ms                                                 | 140 ms: 1.06x slower                                                 |
| sqlglot_transpile          | 1.58 ms                                                | 1.68 ms: 1.06x slower                                                |
| sqlglot_normalize          | 108 ms                                                 | 115 ms: 1.06x slower                                                 |
| nqueens                    | 78.4 ms                                                | 83.5 ms: 1.07x slower                                                |
| genshi_text                | 23.5 ms                                                | 25.2 ms: 1.07x slower                                                |
| sympy_str                  | 275 ms                                                 | 296 ms: 1.08x slower                                                 |
| sqlglot_optimize           | 53.7 ms                                                | 57.8 ms: 1.08x slower                                                |
| sympy_expand               | 463 ms                                                 | 500 ms: 1.08x slower                                                 |
| hexiom                     | 6.16 ms                                                | 6.87 ms: 1.12x slower                                                |
| docutils                   | 2.59 sec                                               | 2.94 sec: 1.13x slower                                               |
| sympy_sum                  | 150 ms                                                 | 171 ms: 1.14x slower                                                 |
| sympy_integrate            | 19.9 ms                                                | 22.7 ms: 1.14x slower                                                |
| generators                 | 29.0 ms                                                | 33.1 ms: 1.14x slower                                                |
| genshi_xml                 | 50.9 ms                                                | 59.8 ms: 1.17x slower                                                |
| pylint                     | 313 ms                                                 | 374 ms: 1.19x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                         |

Benchmark hidden because not significant (8): coverage, bench_mp_pool, pycparser, coroutines, json_loads, pprint_safe_repr, async_tree_io, async_tree_io_tg
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20240912-3.14.0a0-282ab23-JIT/bm-20240912-linux-x86_64-brandtbucher-deopt_tracing-3.14.0a0-282ab23.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.033x faster
# HPT report

- Reliability score: 92.32% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.98x