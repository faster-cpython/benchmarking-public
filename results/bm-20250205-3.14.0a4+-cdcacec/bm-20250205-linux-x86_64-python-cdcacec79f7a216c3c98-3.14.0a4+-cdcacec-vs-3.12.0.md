# Results vs. 3.12.0

- fork: python
- ref: cdcacec79f7a216c3c98
- machine: linux-x86_64
- commit hash: cdcacec
- commit date: 2025-02-05
- overall geometric mean: 1.119x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x faster
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250205-linux-x86_64-python-cdcacec79f7a216c3c98-3.14.0a4+-cdcacec |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 252 ms: 1.09x faster                                                   |
| docutils       | 2.77 sec                                               | 2.58 sec: 1.07x faster                                                 |
| Geometric mean | (ref)                                                  | 1.08x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250205-linux-x86_64-python-cdcacec79f7a216c3c98-3.14.0a4+-cdcacec |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 615 ms: 1.92x faster                                                   |
| async_tree_io              | 1.16 sec                                               | 618 ms: 1.87x faster                                                   |
| async_tree_memoization     | 578 ms                                                 | 322 ms: 1.79x faster                                                   |
| async_tree_memoization_tg  | 575 ms                                                 | 321 ms: 1.79x faster                                                   |
| async_tree_none            | 472 ms                                                 | 264 ms: 1.79x faster                                                   |
| async_tree_none_tg         | 450 ms                                                 | 254 ms: 1.77x faster                                                   |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 488 ms: 1.49x faster                                                   |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 499 ms: 1.45x faster                                                   |
| Geometric mean             | (ref)                                                  | 1.73x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250205-linux-x86_64-python-cdcacec79f7a216c3c98-3.14.0a4+-cdcacec |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 70.5 ms: 1.20x faster                                                  |
| nbody          | 97.0 ms                                                | 92.7 ms: 1.05x faster                                                  |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                  | 1.08x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250205-linux-x86_64-python-cdcacec79f7a216c3c98-3.14.0a4+-cdcacec |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 126 ms: 1.18x faster                                                   |
| regex_effbot   | 3.61 ms                                                | 3.30 ms: 1.09x faster                                                  |
| regex_dna      | 212 ms                                                 | 210 ms: 1.01x faster                                                   |
| regex_v8       | 23.1 ms                                                | 25.4 ms: 1.10x slower                                                  |
| Geometric mean | (ref)                                                  | 1.04x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250205-linux-x86_64-python-cdcacec79f7a216c3c98-3.14.0a4+-cdcacec |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.94 sec: 1.20x faster                                                 |
| xml_etree_parse      | 159 ms                                                 | 139 ms: 1.14x faster                                                   |
| xml_etree_iterparse  | 107 ms                                                 | 97.1 ms: 1.10x faster                                                  |
| xml_etree_generate   | 89.2 ms                                                | 82.9 ms: 1.08x faster                                                  |
| unpickle_pure_python | 230 us                                                 | 216 us: 1.07x faster                                                   |
| xml_etree_process    | 61.7 ms                                                | 58.4 ms: 1.06x faster                                                  |
| pickle_pure_python   | 324 us                                                 | 317 us: 1.02x faster                                                   |
| json_dumps           | 10.4 ms                                                | 11.9 ms: 1.15x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                           |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250205-linux-x86_64-python-cdcacec79f7a216c3c98-3.14.0a4+-cdcacec |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.05 ms: 1.02x slower                                                  |
| python_startup         | 9.55 ms                                                | 12.8 ms: 1.34x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.17x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250205-linux-x86_64-python-cdcacec79f7a216c3c98-3.14.0a4+-cdcacec |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 31.4 ms: 1.10x faster                                                  |
| mako            | 11.9 ms                                                | 11.0 ms: 1.08x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.09x faster                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250205-linux-x86_64-python-cdcacec79f7a216c3c98-3.14.0a4+-cdcacec |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 615 ms: 1.92x faster                                                   |
| async_tree_io              | 1.16 sec                                               | 618 ms: 1.87x faster                                                   |
| async_tree_memoization     | 578 ms                                                 | 322 ms: 1.79x faster                                                   |
| async_tree_memoization_tg  | 575 ms                                                 | 321 ms: 1.79x faster                                                   |
| async_tree_none            | 472 ms                                                 | 264 ms: 1.79x faster                                                   |
| async_tree_none_tg         | 450 ms                                                 | 254 ms: 1.77x faster                                                   |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 488 ms: 1.49x faster                                                   |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 499 ms: 1.45x faster                                                   |
| deepcopy                   | 371 us                                                 | 255 us: 1.45x faster                                                   |
| deepcopy_memo              | 40.7 us                                                | 30.0 us: 1.36x faster                                                  |
| comprehensions             | 21.8 us                                                | 16.3 us: 1.34x faster                                                  |
| deepcopy_reduce            | 3.35 us                                                | 2.68 us: 1.25x faster                                                  |
| async_generators           | 463 ms                                                 | 383 ms: 1.21x faster                                                   |
| spectral_norm              | 115 ms                                                 | 95.1 ms: 1.21x faster                                                  |
| float                      | 84.7 ms                                                | 70.5 ms: 1.20x faster                                                  |
| pathlib                    | 19.3 ms                                                | 16.1 ms: 1.20x faster                                                  |
| tomli_loads                | 2.33 sec                                               | 1.94 sec: 1.20x faster                                                 |
| logging_format             | 7.23 us                                                | 6.12 us: 1.18x faster                                                  |
| logging_simple             | 6.46 us                                                | 5.48 us: 1.18x faster                                                  |
| regex_compile              | 148 ms                                                 | 126 ms: 1.18x faster                                                   |
| go                         | 139 ms                                                 | 119 ms: 1.17x faster                                                   |
| crypto_pyaes               | 81.9 ms                                                | 70.2 ms: 1.17x faster                                                  |
| raytrace                   | 312 ms                                                 | 269 ms: 1.16x faster                                                   |
| chaos                      | 67.0 ms                                                | 57.6 ms: 1.16x faster                                                  |
| sympy_sum                  | 169 ms                                                 | 147 ms: 1.15x faster                                                   |
| deltablue                  | 3.72 ms                                                | 3.22 ms: 1.15x faster                                                  |
| sqlalchemy_declarative     | 147 ms                                                 | 128 ms: 1.15x faster                                                   |
| xml_etree_parse            | 159 ms                                                 | 139 ms: 1.14x faster                                                   |
| sqlalchemy_imperative      | 18.7 ms                                                | 16.4 ms: 1.14x faster                                                  |
| sympy_str                  | 300 ms                                                 | 265 ms: 1.13x faster                                                   |
| generators                 | 31.2 ms                                                | 27.6 ms: 1.13x faster                                                  |
| scimark_fft                | 382 ms                                                 | 341 ms: 1.12x faster                                                   |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.53 ms: 1.12x faster                                                  |
| scimark_monte_carlo        | 75.1 ms                                                | 67.4 ms: 1.11x faster                                                  |
| django_template            | 34.6 ms                                                | 31.4 ms: 1.10x faster                                                  |
| xml_etree_iterparse        | 107 ms                                                 | 97.1 ms: 1.10x faster                                                  |
| sympy_integrate            | 21.4 ms                                                | 19.5 ms: 1.10x faster                                                  |
| pprint_safe_repr           | 776 ms                                                 | 707 ms: 1.10x faster                                                   |
| regex_effbot               | 3.61 ms                                                | 3.30 ms: 1.09x faster                                                  |
| 2to3                       | 274 ms                                                 | 252 ms: 1.09x faster                                                   |
| pprint_pformat             | 1.57 sec                                               | 1.45 sec: 1.08x faster                                                 |
| mako                       | 11.9 ms                                                | 11.0 ms: 1.08x faster                                                  |
| sqlglot_transpile          | 1.68 ms                                                | 1.56 ms: 1.08x faster                                                  |
| sqlglot_parse              | 1.36 ms                                                | 1.26 ms: 1.08x faster                                                  |
| xml_etree_generate         | 89.2 ms                                                | 82.9 ms: 1.08x faster                                                  |
| sqlglot_normalize          | 110 ms                                                 | 103 ms: 1.07x faster                                                   |
| docutils                   | 2.77 sec                                               | 2.58 sec: 1.07x faster                                                 |
| dulwich_log                | 68.5 ms                                                | 64.0 ms: 1.07x faster                                                  |
| mdp                        | 2.63 sec                                               | 2.46 sec: 1.07x faster                                                 |
| scimark_sor                | 129 ms                                                 | 121 ms: 1.07x faster                                                   |
| pyflate                    | 482 ms                                                 | 452 ms: 1.07x faster                                                   |
| unpickle_pure_python       | 230 us                                                 | 216 us: 1.07x faster                                                   |
| meteor_contest             | 112 ms                                                 | 106 ms: 1.06x faster                                                   |
| sqlglot_optimize           | 54.8 ms                                                | 51.8 ms: 1.06x faster                                                  |
| xml_etree_process          | 61.7 ms                                                | 58.4 ms: 1.06x faster                                                  |
| sympy_expand               | 478 ms                                                 | 454 ms: 1.05x faster                                                   |
| fannkuch                   | 417 ms                                                 | 396 ms: 1.05x faster                                                   |
| nqueens                    | 83.3 ms                                                | 79.6 ms: 1.05x faster                                                  |
| richards                   | 45.8 ms                                                | 43.8 ms: 1.05x faster                                                  |
| nbody                      | 97.0 ms                                                | 92.7 ms: 1.05x faster                                                  |
| scimark_lu                 | 118 ms                                                 | 115 ms: 1.03x faster                                                   |
| richards_super             | 51.5 ms                                                | 50.2 ms: 1.03x faster                                                  |
| json                       | 5.26 ms                                                | 5.14 ms: 1.02x faster                                                  |
| hexiom                     | 6.41 ms                                                | 6.27 ms: 1.02x faster                                                  |
| pickle_pure_python         | 324 us                                                 | 317 us: 1.02x faster                                                   |
| sqlite_synth               | 2.83 us                                                | 2.77 us: 1.02x faster                                                  |
| pycparser                  | 1.18 sec                                               | 1.16 sec: 1.02x faster                                                 |
| regex_dna                  | 212 ms                                                 | 210 ms: 1.01x faster                                                   |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                                   |
| coroutines                 | 23.2 ms                                                | 23.3 ms: 1.01x slower                                                  |
| python_startup_no_site     | 6.94 ms                                                | 7.05 ms: 1.02x slower                                                  |
| bench_thread_pool          | 842 us                                                 | 864 us: 1.03x slower                                                   |
| logging_silent             | 104 ns                                                 | 107 ns: 1.03x slower                                                   |
| regex_v8                   | 23.1 ms                                                | 25.4 ms: 1.10x slower                                                  |
| telco                      | 7.10 ms                                                | 7.81 ms: 1.10x slower                                                  |
| json_dumps                 | 10.4 ms                                                | 11.9 ms: 1.15x slower                                                  |
| coverage                   | 72.7 ms                                                | 91.8 ms: 1.26x slower                                                  |
| gc_traversal               | 3.79 ms                                                | 5.03 ms: 1.33x slower                                                  |
| python_startup             | 9.55 ms                                                | 12.8 ms: 1.34x slower                                                  |
| create_gc_cycles           | 1.48 ms                                                | 2.48 ms: 1.68x slower                                                  |
| bench_mp_pool              | 24.0 ms                                                | 81.0 ms: 3.37x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.10x faster                                                           |

Benchmark hidden because not significant (3): typing_runtime_protocols, json_loads, asyncio_websockets
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250205-3.14.0a4+-cdcacec/bm-20250205-linux-x86_64-python-cdcacec79f7a216c3c98-3.14.0a4+-cdcacec.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.119x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.07x
- 95% likely to have a speedup of 1.07x
- 99% likely to have a speedup of 1.06x

# Memory
- memory change: 1.09x