# Results vs. 3.13.0

- fork: mdboom
- ref: marshal_slice
- machine: linux-x86_64
- commit hash: 0e19ac7
- commit date: 2024-10-07
- overall geometric mean: 1.025x faster
- HPT reliability: 87.41%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.96x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 277 ms: 1.04x slower                                           |
| docutils       | 2.59 sec                                               | 2.93 sec: 1.13x slower                                         |
| html5lib       | 64.2 ms                                                | 64.5 ms: 1.01x slower                                          |
| tornado_http   | 92.4 ms                                                | 94.5 ms: 1.02x slower                                          |
| Geometric mean | (ref)                                                  | 1.05x slower                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|---------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| async_tree_memoization_tg | 464 ms                                                 | 403 ms: 1.15x faster                                           |
| async_tree_memoization    | 442 ms                                                 | 401 ms: 1.10x faster                                           |
| async_tree_none           | 351 ms                                                 | 331 ms: 1.06x faster                                           |
| async_tree_none_tg        | 321 ms                                                 | 310 ms: 1.03x faster                                           |
| async_tree_cpu_io_mixed   | 577 ms                                                 | 570 ms: 1.01x faster                                           |
| asyncio_websockets        | 552 ms                                                 | 556 ms: 1.01x slower                                           |
| async_generators          | 436 ms                                                 | 460 ms: 1.06x slower                                           |
| async_tree_io_tg          | 857 ms                                                 | 915 ms: 1.07x slower                                           |
| async_tree_io             | 842 ms                                                 | 937 ms: 1.11x slower                                           |
| Geometric mean            | (ref)                                                  | 1.01x faster                                                   |

Benchmark hidden because not significant (2): coroutines, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| float          | 79.2 ms                                                | 72.2 ms: 1.10x faster                                          |
| nbody          | 87.0 ms                                                | 80.7 ms: 1.08x faster                                          |
| pidigits       | 186 ms                                                 | 185 ms: 1.01x faster                                           |
| Geometric mean | (ref)                                                  | 1.06x faster                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                | 24.1 ms: 1.09x faster                                          |
| regex_effbot   | 3.73 ms                                                | 3.77 ms: 1.01x slower                                          |
| regex_compile  | 132 ms                                                 | 143 ms: 1.08x slower                                           |
| Geometric mean | (ref)                                                  | 1.00x slower                                                   |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| xml_etree_generate   | 86.7 ms                                                | 77.2 ms: 1.12x faster                                          |
| tomli_loads          | 2.14 sec                                               | 1.91 sec: 1.12x faster                                         |
| xml_etree_process    | 60.6 ms                                                | 54.4 ms: 1.11x faster                                          |
| xml_etree_parse      | 156 ms                                                 | 144 ms: 1.08x faster                                           |
| json_dumps           | 10.6 ms                                                | 10.0 ms: 1.05x faster                                          |
| json_loads           | 27.2 us                                                | 26.6 us: 1.02x faster                                          |
| xml_etree_iterparse  | 101 ms                                                 | 99.1 ms: 1.02x faster                                          |
| pickle_pure_python   | 310 us                                                 | 307 us: 1.01x faster                                           |
| unpickle_pure_python | 216 us                                                 | 217 us: 1.01x slower                                           |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| python_startup         | 12.5 ms                                                | 10.6 ms: 1.18x faster                                          |
| python_startup_no_site | 6.96 ms                                                | 7.09 ms: 1.02x slower                                          |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 10.0 ms: 1.11x faster                                          |
| django_template | 35.2 ms                                                | 35.5 ms: 1.01x slower                                          |
| genshi_text     | 23.5 ms                                                | 25.5 ms: 1.08x slower                                          |
| genshi_xml      | 50.9 ms                                                | 58.3 ms: 1.15x slower                                          |
| Geometric mean  | (ref)                                                  | 1.03x slower                                                   |

All benchmarks:
===============

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|---------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| deepcopy_memo             | 39.1 us                                                | 26.9 us: 1.45x faster                                          |
| deepcopy                  | 358 us                                                 | 266 us: 1.35x faster                                           |
| create_gc_cycles          | 2.41 ms                                                | 1.80 ms: 1.34x faster                                          |
| deepcopy_reduce           | 3.20 us                                                | 2.66 us: 1.20x faster                                          |
| python_startup            | 12.5 ms                                                | 10.6 ms: 1.18x faster                                          |
| scimark_fft               | 364 ms                                                 | 310 ms: 1.17x faster                                           |
| richards_super            | 54.9 ms                                                | 46.9 ms: 1.17x faster                                          |
| gc_traversal              | 4.37 ms                                                | 3.78 ms: 1.16x faster                                          |
| async_tree_memoization_tg | 464 ms                                                 | 403 ms: 1.15x faster                                           |
| crypto_pyaes              | 75.3 ms                                                | 65.8 ms: 1.14x faster                                          |
| richards                  | 48.7 ms                                                | 42.6 ms: 1.14x faster                                          |
| scimark_sparse_mat_mult   | 5.04 ms                                                | 4.42 ms: 1.14x faster                                          |
| telco                     | 8.54 ms                                                | 7.56 ms: 1.13x faster                                          |
| spectral_norm             | 115 ms                                                 | 102 ms: 1.13x faster                                           |
| xml_etree_generate        | 86.7 ms                                                | 77.2 ms: 1.12x faster                                          |
| tomli_loads               | 2.14 sec                                               | 1.91 sec: 1.12x faster                                         |
| xml_etree_process         | 60.6 ms                                                | 54.4 ms: 1.11x faster                                          |
| mako                      | 11.1 ms                                                | 10.0 ms: 1.11x faster                                          |
| async_tree_memoization    | 442 ms                                                 | 401 ms: 1.10x faster                                           |
| pathlib                   | 17.5 ms                                                | 15.9 ms: 1.10x faster                                          |
| bpe_tokeniser             | 4.75 sec                                               | 4.32 sec: 1.10x faster                                         |
| float                     | 79.2 ms                                                | 72.2 ms: 1.10x faster                                          |
| fannkuch                  | 404 ms                                                 | 369 ms: 1.10x faster                                           |
| go                        | 144 ms                                                 | 132 ms: 1.09x faster                                           |
| regex_v8                  | 26.2 ms                                                | 24.1 ms: 1.09x faster                                          |
| xml_etree_parse           | 156 ms                                                 | 144 ms: 1.08x faster                                           |
| nbody                     | 87.0 ms                                                | 80.7 ms: 1.08x faster                                          |
| pyflate                   | 471 ms                                                 | 439 ms: 1.07x faster                                           |
| mdp                       | 2.72 sec                                               | 2.54 sec: 1.07x faster                                         |
| scimark_monte_carlo       | 67.4 ms                                                | 63.3 ms: 1.07x faster                                          |
| async_tree_none           | 351 ms                                                 | 331 ms: 1.06x faster                                           |
| json_dumps                | 10.6 ms                                                | 10.0 ms: 1.05x faster                                          |
| scimark_sor               | 124 ms                                                 | 118 ms: 1.05x faster                                           |
| meteor_contest            | 109 ms                                                 | 105 ms: 1.04x faster                                           |
| async_tree_none_tg        | 321 ms                                                 | 310 ms: 1.03x faster                                           |
| pycparser                 | 1.20 sec                                               | 1.16 sec: 1.03x faster                                         |
| thrift                    | 809 us                                                 | 783 us: 1.03x faster                                           |
| json                      | 5.36 ms                                                | 5.19 ms: 1.03x faster                                          |
| logging_format            | 6.40 us                                                | 6.20 us: 1.03x faster                                          |
| json_loads                | 27.2 us                                                | 26.6 us: 1.02x faster                                          |
| pprint_safe_repr          | 728 ms                                                 | 712 ms: 1.02x faster                                           |
| xml_etree_iterparse       | 101 ms                                                 | 99.1 ms: 1.02x faster                                          |
| async_tree_cpu_io_mixed   | 577 ms                                                 | 570 ms: 1.01x faster                                           |
| pickle_pure_python        | 310 us                                                 | 307 us: 1.01x faster                                           |
| logging_simple            | 5.72 us                                                | 5.66 us: 1.01x faster                                          |
| logging_silent            | 102 ns                                                 | 101 ns: 1.01x faster                                           |
| scimark_lu                | 113 ms                                                 | 112 ms: 1.01x faster                                           |
| pidigits                  | 186 ms                                                 | 185 ms: 1.01x faster                                           |
| html5lib                  | 64.2 ms                                                | 64.5 ms: 1.01x slower                                          |
| unpickle_pure_python      | 216 us                                                 | 217 us: 1.01x slower                                           |
| asyncio_websockets        | 552 ms                                                 | 556 ms: 1.01x slower                                           |
| django_template           | 35.2 ms                                                | 35.5 ms: 1.01x slower                                          |
| regex_effbot              | 3.73 ms                                                | 3.77 ms: 1.01x slower                                          |
| typing_runtime_protocols  | 165 us                                                 | 167 us: 1.01x slower                                           |
| coverage                  | 84.0 ms                                                | 85.3 ms: 1.02x slower                                          |
| python_startup_no_site    | 6.96 ms                                                | 7.09 ms: 1.02x slower                                          |
| tornado_http              | 92.4 ms                                                | 94.5 ms: 1.02x slower                                          |
| chaos                     | 58.1 ms                                                | 59.4 ms: 1.02x slower                                          |
| comprehensions            | 16.5 us                                                | 17.0 us: 1.03x slower                                          |
| raytrace                  | 267 ms                                                 | 277 ms: 1.04x slower                                           |
| 2to3                      | 267 ms                                                 | 277 ms: 1.04x slower                                           |
| dulwich_log               | 64.3 ms                                                | 67.3 ms: 1.05x slower                                          |
| async_generators          | 436 ms                                                 | 460 ms: 1.06x slower                                           |
| sqlglot_transpile         | 1.58 ms                                                | 1.69 ms: 1.07x slower                                          |
| async_tree_io_tg          | 857 ms                                                 | 915 ms: 1.07x slower                                           |
| sqlglot_parse             | 1.27 ms                                                | 1.36 ms: 1.07x slower                                          |
| sqlglot_normalize         | 108 ms                                                 | 116 ms: 1.08x slower                                           |
| genshi_text               | 23.5 ms                                                | 25.5 ms: 1.08x slower                                          |
| bench_thread_pool         | 822 us                                                 | 890 us: 1.08x slower                                           |
| regex_compile             | 132 ms                                                 | 143 ms: 1.08x slower                                           |
| sympy_expand              | 463 ms                                                 | 502 ms: 1.08x slower                                           |
| sympy_str                 | 275 ms                                                 | 301 ms: 1.09x slower                                           |
| nqueens                   | 78.4 ms                                                | 86.7 ms: 1.11x slower                                          |
| async_tree_io             | 842 ms                                                 | 937 ms: 1.11x slower                                           |
| sqlglot_optimize          | 53.7 ms                                                | 60.4 ms: 1.12x slower                                          |
| docutils                  | 2.59 sec                                               | 2.93 sec: 1.13x slower                                         |
| hexiom                    | 6.16 ms                                                | 6.97 ms: 1.13x slower                                          |
| genshi_xml                | 50.9 ms                                                | 58.3 ms: 1.15x slower                                          |
| sympy_sum                 | 150 ms                                                 | 175 ms: 1.16x slower                                           |
| sympy_integrate           | 19.9 ms                                                | 23.3 ms: 1.17x slower                                          |
| pylint                    | 313 ms                                                 | 375 ms: 1.20x slower                                           |
| generators                | 29.0 ms                                                | 35.0 ms: 1.21x slower                                          |
| bench_mp_pool             | 24.0 ms                                                | 61.2 ms: 2.55x slower                                          |
| Geometric mean            | (ref)                                                  | 1.01x faster                                                   |

Benchmark hidden because not significant (5): coroutines, pprint_pformat, deltablue, regex_dna, async_tree_cpu_io_mixed_tg
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20241007-3.14.0a0-0e19ac7-JIT/bm-20241007-linux-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.025x faster
# HPT report

- Reliability score: 87.41% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.96x