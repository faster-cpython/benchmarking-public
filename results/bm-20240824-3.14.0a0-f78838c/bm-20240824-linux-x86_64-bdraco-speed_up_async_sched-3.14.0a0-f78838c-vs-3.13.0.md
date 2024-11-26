# Results vs. 3.13.0

- fork: bdraco
- ref: speed_up_async_sched
- machine: linux-x86_64
- commit hash: f78838c
- commit date: 2024-08-24
- overall geometric mean: 1.034x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.92x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240824-linux-x86_64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 255 ms: 1.05x faster                                                  |
| docutils       | 2.59 sec                                               | 2.69 sec: 1.04x slower                                                |
| html5lib       | 64.2 ms                                                | 65.2 ms: 1.02x slower                                                 |
| tornado_http   | 92.4 ms                                                | 89.9 ms: 1.03x faster                                                 |
| Geometric mean | (ref)                                                  | 1.01x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240824-linux-x86_64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|---------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg | 464 ms                                                 | 402 ms: 1.15x faster                                                  |
| async_tree_memoization    | 442 ms                                                 | 402 ms: 1.10x faster                                                  |
| async_tree_none           | 351 ms                                                 | 321 ms: 1.09x faster                                                  |
| async_tree_cpu_io_mixed   | 577 ms                                                 | 544 ms: 1.06x faster                                                  |
| async_tree_none_tg        | 321 ms                                                 | 307 ms: 1.04x faster                                                  |
| coroutines                | 22.7 ms                                                | 22.9 ms: 1.01x slower                                                 |
| asyncio_websockets        | 552 ms                                                 | 559 ms: 1.01x slower                                                  |
| async_tree_io_tg          | 857 ms                                                 | 903 ms: 1.05x slower                                                  |
| async_tree_io             | 842 ms                                                 | 891 ms: 1.06x slower                                                  |
| Geometric mean            | (ref)                                                  | 1.03x faster                                                          |

Benchmark hidden because not significant (2): async_generators, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240824-linux-x86_64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 79.2 ms                                                | 77.7 ms: 1.02x faster                                                 |
| nbody          | 87.0 ms                                                | 85.5 ms: 1.02x faster                                                 |
| Geometric mean | (ref)                                                  | 1.01x faster                                                          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240824-linux-x86_64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                | 24.1 ms: 1.09x faster                                                 |
| regex_effbot   | 3.73 ms                                                | 3.58 ms: 1.04x faster                                                 |
| regex_compile  | 132 ms                                                 | 128 ms: 1.03x faster                                                  |
| regex_dna      | 218 ms                                                 | 220 ms: 1.01x slower                                                  |
| Geometric mean | (ref)                                                  | 1.04x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240824-linux-x86_64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_process    | 60.6 ms                                                | 58.2 ms: 1.04x faster                                                 |
| tomli_loads          | 2.14 sec                                               | 2.07 sec: 1.04x faster                                                |
| xml_etree_generate   | 86.7 ms                                                | 83.8 ms: 1.03x faster                                                 |
| pickle_pure_python   | 310 us                                                 | 301 us: 1.03x faster                                                  |
| json_dumps           | 10.6 ms                                                | 10.3 ms: 1.02x faster                                                 |
| unpickle_pure_python | 216 us                                                 | 213 us: 1.01x faster                                                  |
| xml_etree_iterparse  | 101 ms                                                 | 104 ms: 1.03x slower                                                  |
| json_loads           | 27.2 us                                                | 28.2 us: 1.04x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.01x faster                                                          |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240824-linux-x86_64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 12.5 ms                                                | 10.5 ms: 1.18x faster                                                 |
| python_startup_no_site | 6.96 ms                                                | 7.10 ms: 1.02x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240824-linux-x86_64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 23.5 ms                                                | 21.8 ms: 1.08x faster                                                 |
| django_template | 35.2 ms                                                | 33.7 ms: 1.04x faster                                                 |
| genshi_xml      | 50.9 ms                                                | 49.5 ms: 1.03x faster                                                 |
| mako            | 11.1 ms                                                | 11.1 ms: 1.00x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.04x faster                                                          |

All benchmarks:
===============

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240824-linux-x86_64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|---------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy                  | 358 us                                                 | 259 us: 1.38x faster                                                  |
| create_gc_cycles          | 2.41 ms                                                | 1.76 ms: 1.37x faster                                                 |
| deepcopy_memo             | 39.1 us                                                | 29.5 us: 1.33x faster                                                 |
| deepcopy_reduce           | 3.20 us                                                | 2.64 us: 1.21x faster                                                 |
| python_startup            | 12.5 ms                                                | 10.5 ms: 1.18x faster                                                 |
| gc_traversal              | 4.37 ms                                                | 3.75 ms: 1.17x faster                                                 |
| async_tree_memoization_tg | 464 ms                                                 | 402 ms: 1.15x faster                                                  |
| pathlib                   | 17.5 ms                                                | 15.7 ms: 1.12x faster                                                 |
| async_tree_memoization    | 442 ms                                                 | 402 ms: 1.10x faster                                                  |
| async_tree_none           | 351 ms                                                 | 321 ms: 1.09x faster                                                  |
| regex_v8                  | 26.2 ms                                                | 24.1 ms: 1.09x faster                                                 |
| genshi_text               | 23.5 ms                                                | 21.8 ms: 1.08x faster                                                 |
| mdp                       | 2.72 sec                                               | 2.53 sec: 1.08x faster                                                |
| async_tree_cpu_io_mixed   | 577 ms                                                 | 544 ms: 1.06x faster                                                  |
| logging_format            | 6.40 us                                                | 6.03 us: 1.06x faster                                                 |
| scimark_sparse_mat_mult   | 5.04 ms                                                | 4.76 ms: 1.06x faster                                                 |
| thrift                    | 809 us                                                 | 764 us: 1.06x faster                                                  |
| richards_super            | 54.9 ms                                                | 52.0 ms: 1.05x faster                                                 |
| pycparser                 | 1.20 sec                                               | 1.14 sec: 1.05x faster                                                |
| richards                  | 48.7 ms                                                | 46.2 ms: 1.05x faster                                                 |
| generators                | 29.0 ms                                                | 27.6 ms: 1.05x faster                                                 |
| bench_thread_pool         | 822 us                                                 | 783 us: 1.05x faster                                                  |
| 2to3                      | 267 ms                                                 | 255 ms: 1.05x faster                                                  |
| crypto_pyaes              | 75.3 ms                                                | 72.0 ms: 1.05x faster                                                 |
| logging_simple            | 5.72 us                                                | 5.48 us: 1.04x faster                                                 |
| async_tree_none_tg        | 321 ms                                                 | 307 ms: 1.04x faster                                                  |
| xml_etree_process         | 60.6 ms                                                | 58.2 ms: 1.04x faster                                                 |
| django_template           | 35.2 ms                                                | 33.7 ms: 1.04x faster                                                 |
| regex_effbot              | 3.73 ms                                                | 3.58 ms: 1.04x faster                                                 |
| typing_runtime_protocols  | 165 us                                                 | 159 us: 1.04x faster                                                  |
| tomli_loads               | 2.14 sec                                               | 2.07 sec: 1.04x faster                                                |
| spectral_norm             | 115 ms                                                 | 111 ms: 1.04x faster                                                  |
| sympy_str                 | 275 ms                                                 | 265 ms: 1.04x faster                                                  |
| xml_etree_generate        | 86.7 ms                                                | 83.8 ms: 1.03x faster                                                 |
| pickle_pure_python        | 310 us                                                 | 301 us: 1.03x faster                                                  |
| sympy_sum                 | 150 ms                                                 | 146 ms: 1.03x faster                                                  |
| regex_compile             | 132 ms                                                 | 128 ms: 1.03x faster                                                  |
| genshi_xml                | 50.9 ms                                                | 49.5 ms: 1.03x faster                                                 |
| tornado_http              | 92.4 ms                                                | 89.9 ms: 1.03x faster                                                 |
| sympy_expand              | 463 ms                                                 | 451 ms: 1.03x faster                                                  |
| json_dumps                | 10.6 ms                                                | 10.3 ms: 1.02x faster                                                 |
| sympy_integrate           | 19.9 ms                                                | 19.5 ms: 1.02x faster                                                 |
| meteor_contest            | 109 ms                                                 | 107 ms: 1.02x faster                                                  |
| telco                     | 8.54 ms                                                | 8.36 ms: 1.02x faster                                                 |
| float                     | 79.2 ms                                                | 77.7 ms: 1.02x faster                                                 |
| raytrace                  | 267 ms                                                 | 262 ms: 1.02x faster                                                  |
| pprint_pformat            | 1.49 sec                                               | 1.47 sec: 1.02x faster                                                |
| nbody                     | 87.0 ms                                                | 85.5 ms: 1.02x faster                                                 |
| deltablue                 | 3.23 ms                                                | 3.18 ms: 1.02x faster                                                 |
| unpickle_pure_python      | 216 us                                                 | 213 us: 1.01x faster                                                  |
| pprint_safe_repr          | 728 ms                                                 | 720 ms: 1.01x faster                                                  |
| sqlglot_transpile         | 1.58 ms                                                | 1.57 ms: 1.01x faster                                                 |
| sqlglot_normalize         | 108 ms                                                 | 107 ms: 1.01x faster                                                  |
| hexiom                    | 6.16 ms                                                | 6.11 ms: 1.01x faster                                                 |
| sqlglot_optimize          | 53.7 ms                                                | 53.3 ms: 1.01x faster                                                 |
| logging_silent            | 102 ns                                                 | 101 ns: 1.01x faster                                                  |
| scimark_fft               | 364 ms                                                 | 365 ms: 1.00x slower                                                  |
| mako                      | 11.1 ms                                                | 11.1 ms: 1.00x slower                                                 |
| regex_dna                 | 218 ms                                                 | 220 ms: 1.01x slower                                                  |
| nqueens                   | 78.4 ms                                                | 79.3 ms: 1.01x slower                                                 |
| coroutines                | 22.7 ms                                                | 22.9 ms: 1.01x slower                                                 |
| asyncio_websockets        | 552 ms                                                 | 559 ms: 1.01x slower                                                  |
| html5lib                  | 64.2 ms                                                | 65.2 ms: 1.02x slower                                                 |
| coverage                  | 84.0 ms                                                | 85.4 ms: 1.02x slower                                                 |
| bpe_tokeniser             | 4.75 sec                                               | 4.84 sec: 1.02x slower                                                |
| python_startup_no_site    | 6.96 ms                                                | 7.10 ms: 1.02x slower                                                 |
| scimark_sor               | 124 ms                                                 | 127 ms: 1.02x slower                                                  |
| xml_etree_iterparse       | 101 ms                                                 | 104 ms: 1.03x slower                                                  |
| docutils                  | 2.59 sec                                               | 2.69 sec: 1.04x slower                                                |
| json_loads                | 27.2 us                                                | 28.2 us: 1.04x slower                                                 |
| async_tree_io_tg          | 857 ms                                                 | 903 ms: 1.05x slower                                                  |
| async_tree_io             | 842 ms                                                 | 891 ms: 1.06x slower                                                  |
| go                        | 144 ms                                                 | 162 ms: 1.13x slower                                                  |
| Geometric mean            | (ref)                                                  | 1.04x faster                                                          |

Benchmark hidden because not significant (14): fannkuch, json, async_generators, scimark_monte_carlo, pyflate, comprehensions, bench_mp_pool, xml_etree_parse, pidigits, sqlglot_parse, scimark_lu, async_tree_cpu_io_mixed_tg, chaos, pylint
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, dulwich_log, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (2) of results/bm-20240824-3.14.0a0-f78838c/bm-20240824-linux-x86_64-bdraco-speed_up_async_sched-3.14.0a0-f78838c.json: asyncio_tcp, asyncio_tcp_ssl

- Geometric mean (including insignificant results): 1.034x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.92x