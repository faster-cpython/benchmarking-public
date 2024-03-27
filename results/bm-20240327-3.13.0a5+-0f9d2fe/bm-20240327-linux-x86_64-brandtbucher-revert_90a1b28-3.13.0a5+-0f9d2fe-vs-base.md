# Results vs. base

- fork: brandtbucher
- ref: revert_90a1b28
- machine: linux-x86_64
- commit hash: 0f9d2fe
- commit date: 2024-03-27
- overall geometric mean: 1.01x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240327-linux-x86_64-python-74c8568d07719529b874-3.13.0a5+-74c8568 | bm-20240327-linux-x86_64-brandtbucher-revert_90a1b28-3.13.0a5+-0f9d2fe |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 267 ms                                                                 | 267 ms: 1.00x faster                                                   |
| docutils       | 2.77 sec                                                               | 2.76 sec: 1.00x faster                                                 |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                           |

Benchmark hidden because not significant (3): chameleon, html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20240327-linux-x86_64-python-74c8568d07719529b874-3.13.0a5+-74c8568 | bm-20240327-linux-x86_64-brandtbucher-revert_90a1b28-3.13.0a5+-0f9d2fe |
|-------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_none         | 384 ms                                                                 | 368 ms: 1.04x faster                                                   |
| async_tree_io_tg        | 916 ms                                                                 | 898 ms: 1.02x faster                                                   |
| async_tree_cpu_io_mixed | 596 ms                                                                 | 609 ms: 1.02x slower                                                   |
| Geometric mean          | (ref)                                                                  | 1.01x faster                                                           |

Benchmark hidden because not significant (5): async_tree_memoization_tg, async_tree_io, async_tree_memoization, async_tree_cpu_io_mixed_tg, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240327-linux-x86_64-python-74c8568d07719529b874-3.13.0a5+-74c8568 | bm-20240327-linux-x86_64-brandtbucher-revert_90a1b28-3.13.0a5+-0f9d2fe |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 78.6 ms                                                                | 76.7 ms: 1.03x faster                                                  |
| pidigits       | 190 ms                                                                 | 190 ms: 1.00x slower                                                   |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                           |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240327-linux-x86_64-python-74c8568d07719529b874-3.13.0a5+-74c8568 | bm-20240327-linux-x86_64-brandtbucher-revert_90a1b28-3.13.0a5+-0f9d2fe |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_v8       | 26.6 ms                                                                | 25.6 ms: 1.04x faster                                                  |
| regex_dna      | 233 ms                                                                 | 225 ms: 1.03x faster                                                   |
| regex_effbot   | 3.78 ms                                                                | 3.71 ms: 1.02x faster                                                  |
| regex_compile  | 134 ms                                                                 | 134 ms: 1.00x slower                                                   |
| Geometric mean | (ref)                                                                  | 1.02x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240327-linux-x86_64-python-74c8568d07719529b874-3.13.0a5+-74c8568 | bm-20240327-linux-x86_64-brandtbucher-revert_90a1b28-3.13.0a5+-0f9d2fe |
|----------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| unpickle             | 16.6 us                                                                | 14.9 us: 1.12x faster                                                  |
| pickle_list          | 5.33 us                                                                | 4.97 us: 1.07x faster                                                  |
| pickle_dict          | 35.4 us                                                                | 34.3 us: 1.03x faster                                                  |
| unpickle_list        | 5.32 us                                                                | 5.16 us: 1.03x faster                                                  |
| pickle               | 12.0 us                                                                | 11.7 us: 1.03x faster                                                  |
| tomli_loads          | 2.22 sec                                                               | 2.17 sec: 1.02x faster                                                 |
| xml_etree_generate   | 87.2 ms                                                                | 85.8 ms: 1.02x faster                                                  |
| xml_etree_iterparse  | 107 ms                                                                 | 106 ms: 1.01x faster                                                   |
| xml_etree_process    | 59.7 ms                                                                | 59.2 ms: 1.01x faster                                                  |
| pickle_pure_python   | 301 us                                                                 | 299 us: 1.01x faster                                                   |
| json_dumps           | 10.5 ms                                                                | 10.5 ms: 1.00x faster                                                  |
| json_loads           | 28.5 us                                                                | 28.8 us: 1.01x slower                                                  |
| unpickle_pure_python | 218 us                                                                 | 222 us: 1.02x slower                                                   |
| Geometric mean       | (ref)                                                                  | 1.02x faster                                                           |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240327-linux-x86_64-python-74c8568d07719529b874-3.13.0a5+-74c8568 | bm-20240327-linux-x86_64-brandtbucher-revert_90a1b28-3.13.0a5+-0f9d2fe |
|------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 9.00 ms                                                                | 6.89 ms: 1.31x faster                                                  |
| python_startup         | 10.6 ms                                                                | 10.4 ms: 1.02x faster                                                  |
| Geometric mean         | (ref)                                                                  | 1.16x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240327-linux-x86_64-python-74c8568d07719529b874-3.13.0a5+-74c8568 | bm-20240327-linux-x86_64-brandtbucher-revert_90a1b28-3.13.0a5+-0f9d2fe |
|-----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| django_template | 35.1 ms                                                                | 34.2 ms: 1.02x faster                                                  |
| genshi_xml      | 52.0 ms                                                                | 51.7 ms: 1.01x faster                                                  |
| genshi_text     | 24.1 ms                                                                | 24.5 ms: 1.02x slower                                                  |
| Geometric mean  | (ref)                                                                  | 1.00x faster                                                           |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark               | bm-20240327-linux-x86_64-python-74c8568d07719529b874-3.13.0a5+-74c8568 | bm-20240327-linux-x86_64-brandtbucher-revert_90a1b28-3.13.0a5+-0f9d2fe |
|-------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site  | 9.00 ms                                                                | 6.89 ms: 1.31x faster                                                  |
| unpickle                | 16.6 us                                                                | 14.9 us: 1.12x faster                                                  |
| mdp                     | 2.78 sec                                                               | 2.57 sec: 1.08x faster                                                 |
| pickle_list             | 5.33 us                                                                | 4.97 us: 1.07x faster                                                  |
| async_tree_none         | 384 ms                                                                 | 368 ms: 1.04x faster                                                   |
| pycparser               | 1.23 sec                                                               | 1.18 sec: 1.04x faster                                                 |
| regex_v8                | 26.6 ms                                                                | 25.6 ms: 1.04x faster                                                  |
| regex_dna               | 233 ms                                                                 | 225 ms: 1.03x faster                                                   |
| pickle_dict             | 35.4 us                                                                | 34.3 us: 1.03x faster                                                  |
| pyflate                 | 478 ms                                                                 | 463 ms: 1.03x faster                                                   |
| unpickle_list           | 5.32 us                                                                | 5.16 us: 1.03x faster                                                  |
| coroutines              | 23.3 ms                                                                | 22.7 ms: 1.03x faster                                                  |
| pprint_safe_repr        | 756 ms                                                                 | 735 ms: 1.03x faster                                                   |
| coverage                | 97.9 ms                                                                | 95.5 ms: 1.03x faster                                                  |
| pickle                  | 12.0 us                                                                | 11.7 us: 1.03x faster                                                  |
| float                   | 78.6 ms                                                                | 76.7 ms: 1.03x faster                                                  |
| scimark_sparse_mat_mult | 4.92 ms                                                                | 4.80 ms: 1.02x faster                                                  |
| pprint_pformat          | 1.54 sec                                                               | 1.51 sec: 1.02x faster                                                 |
| django_template         | 35.1 ms                                                                | 34.2 ms: 1.02x faster                                                  |
| tomli_loads             | 2.22 sec                                                               | 2.17 sec: 1.02x faster                                                 |
| python_startup          | 10.6 ms                                                                | 10.4 ms: 1.02x faster                                                  |
| async_tree_io_tg        | 916 ms                                                                 | 898 ms: 1.02x faster                                                   |
| spectral_norm           | 110 ms                                                                 | 108 ms: 1.02x faster                                                   |
| regex_effbot            | 3.78 ms                                                                | 3.71 ms: 1.02x faster                                                  |
| comprehensions          | 16.7 us                                                                | 16.5 us: 1.02x faster                                                  |
| xml_etree_generate      | 87.2 ms                                                                | 85.8 ms: 1.02x faster                                                  |
| scimark_lu              | 117 ms                                                                 | 115 ms: 1.01x faster                                                   |
| xml_etree_iterparse     | 107 ms                                                                 | 106 ms: 1.01x faster                                                   |
| meteor_contest          | 110 ms                                                                 | 109 ms: 1.01x faster                                                   |
| telco                   | 8.56 ms                                                                | 8.45 ms: 1.01x faster                                                  |
| sympy_sum               | 154 ms                                                                 | 152 ms: 1.01x faster                                                   |
| json                    | 5.39 ms                                                                | 5.33 ms: 1.01x faster                                                  |
| thrift                  | 814 us                                                                 | 806 us: 1.01x faster                                                   |
| xml_etree_process       | 59.7 ms                                                                | 59.2 ms: 1.01x faster                                                  |
| deltablue               | 3.27 ms                                                                | 3.24 ms: 1.01x faster                                                  |
| deepcopy                | 355 us                                                                 | 352 us: 1.01x faster                                                   |
| sympy_str               | 275 ms                                                                 | 273 ms: 1.01x faster                                                   |
| deepcopy_memo           | 38.8 us                                                                | 38.5 us: 1.01x faster                                                  |
| pickle_pure_python      | 301 us                                                                 | 299 us: 1.01x faster                                                   |
| fannkuch                | 397 ms                                                                 | 394 ms: 1.01x faster                                                   |
| deepcopy_reduce         | 3.18 us                                                                | 3.17 us: 1.01x faster                                                  |
| nqueens                 | 80.8 ms                                                                | 80.3 ms: 1.01x faster                                                  |
| create_gc_cycles        | 1.68 ms                                                                | 1.67 ms: 1.01x faster                                                  |
| genshi_xml              | 52.0 ms                                                                | 51.7 ms: 1.01x faster                                                  |
| pathlib                 | 18.6 ms                                                                | 18.4 ms: 1.01x faster                                                  |
| sympy_integrate         | 20.2 ms                                                                | 20.1 ms: 1.01x faster                                                  |
| richards_super          | 52.5 ms                                                                | 52.2 ms: 1.01x faster                                                  |
| docutils                | 2.77 sec                                                               | 2.76 sec: 1.00x faster                                                 |
| json_dumps              | 10.5 ms                                                                | 10.5 ms: 1.00x faster                                                  |
| 2to3                    | 267 ms                                                                 | 267 ms: 1.00x faster                                                   |
| sqlglot_transpile       | 1.58 ms                                                                | 1.57 ms: 1.00x faster                                                  |
| pidigits                | 190 ms                                                                 | 190 ms: 1.00x slower                                                   |
| asyncio_tcp_ssl         | 1.83 sec                                                               | 1.84 sec: 1.00x slower                                                 |
| bench_thread_pool       | 829 us                                                                 | 831 us: 1.00x slower                                                   |
| regex_compile           | 134 ms                                                                 | 134 ms: 1.00x slower                                                   |
| async_generators        | 443 ms                                                                 | 445 ms: 1.00x slower                                                   |
| raytrace                | 265 ms                                                                 | 266 ms: 1.01x slower                                                   |
| generators              | 29.5 ms                                                                | 29.7 ms: 1.01x slower                                                  |
| scimark_fft             | 363 ms                                                                 | 366 ms: 1.01x slower                                                   |
| logging_format          | 6.48 us                                                                | 6.54 us: 1.01x slower                                                  |
| sqlite_synth            | 2.90 us                                                                | 2.93 us: 1.01x slower                                                  |
| json_loads              | 28.5 us                                                                | 28.8 us: 1.01x slower                                                  |
| hexiom                  | 6.22 ms                                                                | 6.29 ms: 1.01x slower                                                  |
| logging_silent          | 100 ns                                                                 | 101 ns: 1.01x slower                                                   |
| genshi_text             | 24.1 ms                                                                | 24.5 ms: 1.02x slower                                                  |
| logging_simple          | 5.84 us                                                                | 5.95 us: 1.02x slower                                                  |
| crypto_pyaes            | 72.0 ms                                                                | 73.4 ms: 1.02x slower                                                  |
| unpickle_pure_python    | 218 us                                                                 | 222 us: 1.02x slower                                                   |
| gc_traversal            | 3.92 ms                                                                | 4.00 ms: 1.02x slower                                                  |
| async_tree_cpu_io_mixed | 596 ms                                                                 | 609 ms: 1.02x slower                                                   |
| unpack_sequence         | 46.8 ns                                                                | 54.5 ns: 1.16x slower                                                  |
| Geometric mean          | (ref)                                                                  | 1.01x faster                                                           |

Benchmark hidden because not significant (31): async_tree_memoization_tg, async_tree_io, xml_etree_parse, djangocms, nbody, chameleon, typing_runtime_protocols, richards, pylint, async_tree_memoization, html5lib, sympy_expand, scimark_monte_carlo, sqlglot_normalize, aiohttp, bench_mp_pool, sqlglot_parse, sqlglot_optimize, dask, tornado_http, asyncio_websockets, asyncio_tcp, scimark_sor, chaos, go, mako, mypy2, dulwich_log, gunicorn, async_tree_cpu_io_mixed_tg, async_tree_none_tg


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x


# Memory

- memory change: 1.00x