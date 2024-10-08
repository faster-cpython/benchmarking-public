# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: trace_through
- machine: linux-x86_64
- commit hash: b1a2c42
- commit date: 2024-09-06
- overall geometric mean: 1.04x faster
- HPT reliability: 99.98%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240906-linux-x86_64-brandtbucher-trace_through-3.14.0a0-b1a2c42 |
|----------------|:----------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 278 ms: 1.01x slower                                                 |
| docutils       | 2.83 sec                                                   | 3.00 sec: 1.06x slower                                               |
| html5lib       | 67.2 ms                                                    | 62.4 ms: 1.08x faster                                                |
| tornado_http   | 94.6 ms                                                    | 95.7 ms: 1.01x slower                                                |
| Geometric mean | (ref)                                                      | 1.00x slower                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240906-linux-x86_64-brandtbucher-trace_through-3.14.0a0-b1a2c42 |
|----------------------------|:----------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_none            | 378 ms                                                     | 325 ms: 1.16x faster                                                 |
| async_tree_memoization     | 463 ms                                                     | 402 ms: 1.15x faster                                                 |
| async_tree_memoization_tg  | 444 ms                                                     | 401 ms: 1.11x faster                                                 |
| async_tree_none_tg         | 336 ms                                                     | 307 ms: 1.09x faster                                                 |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 562 ms: 1.09x faster                                                 |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 542 ms: 1.08x faster                                                 |
| async_tree_io_tg           | 936 ms                                                     | 889 ms: 1.05x faster                                                 |
| Geometric mean             | (ref)                                                      | 1.09x faster                                                         |

Benchmark hidden because not significant (1): async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240906-linux-x86_64-brandtbucher-trace_through-3.14.0a0-b1a2c42 |
|----------------|:----------------------------------------------------------:|:--------------------------------------------------------------------:|
| float          | 78.9 ms                                                    | 70.3 ms: 1.12x faster                                                |
| nbody          | 88.3 ms                                                    | 81.0 ms: 1.09x faster                                                |
| pidigits       | 191 ms                                                     | 187 ms: 1.02x faster                                                 |
| Geometric mean | (ref)                                                      | 1.08x faster                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240906-linux-x86_64-brandtbucher-trace_through-3.14.0a0-b1a2c42 |
|----------------|:----------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_effbot   | 3.67 ms                                                    | 3.47 ms: 1.06x faster                                                |
| regex_dna      | 221 ms                                                     | 212 ms: 1.04x faster                                                 |
| regex_v8       | 25.1 ms                                                    | 24.4 ms: 1.03x faster                                                |
| regex_compile  | 137 ms                                                     | 145 ms: 1.06x slower                                                 |
| Geometric mean | (ref)                                                      | 1.02x faster                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240906-linux-x86_64-brandtbucher-trace_through-3.14.0a0-b1a2c42 |
|----------------------|:----------------------------------------------------------:|:--------------------------------------------------------------------:|
| xml_etree_generate   | 87.4 ms                                                    | 76.5 ms: 1.14x faster                                                |
| xml_etree_process    | 61.2 ms                                                    | 54.0 ms: 1.13x faster                                                |
| xml_etree_parse      | 162 ms                                                     | 145 ms: 1.12x faster                                                 |
| xml_etree_iterparse  | 107 ms                                                     | 98.5 ms: 1.09x faster                                                |
| tomli_loads          | 2.12 sec                                                   | 1.95 sec: 1.09x faster                                               |
| json_dumps           | 10.7 ms                                                    | 10.3 ms: 1.04x faster                                                |
| unpickle_list        | 5.34 us                                                    | 5.16 us: 1.03x faster                                                |
| unpickle_pure_python | 218 us                                                     | 213 us: 1.02x faster                                                 |
| pickle_pure_python   | 305 us                                                     | 302 us: 1.01x faster                                                 |
| pickle_dict          | 34.8 us                                                    | 34.5 us: 1.01x faster                                                |
| json_loads           | 28.9 us                                                    | 28.7 us: 1.01x faster                                                |
| pickle_list          | 5.11 us                                                    | 5.09 us: 1.00x faster                                                |
| pickle               | 11.5 us                                                    | 11.7 us: 1.02x slower                                                |
| Geometric mean       | (ref)                                                      | 1.05x faster                                                         |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240906-linux-x86_64-brandtbucher-trace_through-3.14.0a0-b1a2c42 |
|------------------------|:----------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.6 ms: 1.01x faster                                                |
| python_startup_no_site | 7.11 ms                                                    | 7.17 ms: 1.01x slower                                                |
| Geometric mean         | (ref)                                                      | 1.00x faster                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240906-linux-x86_64-brandtbucher-trace_through-3.14.0a0-b1a2c42 |
|-----------------|:----------------------------------------------------------:|:--------------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 9.85 ms: 1.14x faster                                                |
| genshi_text     | 23.7 ms                                                    | 24.5 ms: 1.03x slower                                                |
| django_template | 34.8 ms                                                    | 36.6 ms: 1.05x slower                                                |
| genshi_xml      | 51.6 ms                                                    | 55.9 ms: 1.08x slower                                                |
| Geometric mean  | (ref)                                                      | 1.01x slower                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240906-linux-x86_64-brandtbucher-trace_through-3.14.0a0-b1a2c42 |
|----------------------------|:----------------------------------------------------------:|:--------------------------------------------------------------------:|
| deepcopy_memo              | 39.7 us                                                    | 26.4 us: 1.51x faster                                                |
| deepcopy                   | 367 us                                                     | 264 us: 1.39x faster                                                 |
| richards_super             | 57.4 ms                                                    | 44.0 ms: 1.30x faster                                                |
| richards                   | 50.9 ms                                                    | 39.8 ms: 1.28x faster                                                |
| deepcopy_reduce            | 3.35 us                                                    | 2.62 us: 1.28x faster                                                |
| scimark_fft                | 392 ms                                                     | 316 ms: 1.24x faster                                                 |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.43 ms: 1.19x faster                                                |
| async_tree_none            | 378 ms                                                     | 325 ms: 1.16x faster                                                 |
| crypto_pyaes               | 77.5 ms                                                    | 66.7 ms: 1.16x faster                                                |
| spectral_norm              | 116 ms                                                     | 100 ms: 1.16x faster                                                 |
| async_tree_memoization     | 463 ms                                                     | 402 ms: 1.15x faster                                                 |
| xml_etree_generate         | 87.4 ms                                                    | 76.5 ms: 1.14x faster                                                |
| mako                       | 11.2 ms                                                    | 9.85 ms: 1.14x faster                                                |
| xml_etree_process          | 61.2 ms                                                    | 54.0 ms: 1.13x faster                                                |
| float                      | 78.9 ms                                                    | 70.3 ms: 1.12x faster                                                |
| bpe_tokeniser              | 5.02 sec                                                   | 4.50 sec: 1.12x faster                                               |
| xml_etree_parse            | 162 ms                                                     | 145 ms: 1.12x faster                                                 |
| gc_traversal               | 3.98 ms                                                    | 3.59 ms: 1.11x faster                                                |
| async_tree_memoization_tg  | 444 ms                                                     | 401 ms: 1.11x faster                                                 |
| scimark_monte_carlo        | 69.2 ms                                                    | 62.7 ms: 1.10x faster                                                |
| sqlite_synth               | 2.99 us                                                    | 2.72 us: 1.10x faster                                                |
| scimark_sor                | 127 ms                                                     | 116 ms: 1.09x faster                                                 |
| async_tree_none_tg         | 336 ms                                                     | 307 ms: 1.09x faster                                                 |
| pathlib                    | 17.3 ms                                                    | 15.8 ms: 1.09x faster                                                |
| nbody                      | 88.3 ms                                                    | 81.0 ms: 1.09x faster                                                |
| xml_etree_iterparse        | 107 ms                                                     | 98.5 ms: 1.09x faster                                                |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 562 ms: 1.09x faster                                                 |
| coverage                   | 93.1 ms                                                    | 85.8 ms: 1.09x faster                                                |
| tomli_loads                | 2.12 sec                                                   | 1.95 sec: 1.09x faster                                               |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 542 ms: 1.08x faster                                                 |
| pyflate                    | 484 ms                                                     | 449 ms: 1.08x faster                                                 |
| html5lib                   | 67.2 ms                                                    | 62.4 ms: 1.08x faster                                                |
| go                         | 145 ms                                                     | 134 ms: 1.08x faster                                                 |
| fannkuch                   | 402 ms                                                     | 374 ms: 1.07x faster                                                 |
| scimark_lu                 | 122 ms                                                     | 113 ms: 1.07x faster                                                 |
| pprint_safe_repr           | 758 ms                                                     | 716 ms: 1.06x faster                                                 |
| regex_effbot               | 3.67 ms                                                    | 3.47 ms: 1.06x faster                                                |
| thrift                     | 823 us                                                     | 780 us: 1.06x faster                                                 |
| async_tree_io_tg           | 936 ms                                                     | 889 ms: 1.05x faster                                                 |
| telco                      | 8.41 ms                                                    | 7.99 ms: 1.05x faster                                                |
| pprint_pformat             | 1.56 sec                                                   | 1.48 sec: 1.05x faster                                               |
| asyncio_tcp                | 508 ms                                                     | 485 ms: 1.05x faster                                                 |
| logging_silent             | 105 ns                                                     | 100.0 ns: 1.05x faster                                               |
| deltablue                  | 3.25 ms                                                    | 3.11 ms: 1.05x faster                                                |
| chaos                      | 61.3 ms                                                    | 58.7 ms: 1.05x faster                                                |
| regex_dna                  | 221 ms                                                     | 212 ms: 1.04x faster                                                 |
| logging_format             | 6.47 us                                                    | 6.22 us: 1.04x faster                                                |
| json_dumps                 | 10.7 ms                                                    | 10.3 ms: 1.04x faster                                                |
| unpickle_list              | 5.34 us                                                    | 5.16 us: 1.03x faster                                                |
| create_gc_cycles           | 1.82 ms                                                    | 1.76 ms: 1.03x faster                                                |
| regex_v8                   | 25.1 ms                                                    | 24.4 ms: 1.03x faster                                                |
| unpickle_pure_python       | 218 us                                                     | 213 us: 1.02x faster                                                 |
| mdp                        | 2.79 sec                                                   | 2.72 sec: 1.02x faster                                               |
| asyncio_websockets         | 567 ms                                                     | 554 ms: 1.02x faster                                                 |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.80 sec: 1.02x faster                                               |
| pidigits                   | 191 ms                                                     | 187 ms: 1.02x faster                                                 |
| logging_simple             | 5.74 us                                                    | 5.67 us: 1.01x faster                                                |
| python_startup             | 10.8 ms                                                    | 10.6 ms: 1.01x faster                                                |
| pickle_pure_python         | 305 us                                                     | 302 us: 1.01x faster                                                 |
| pickle_dict                | 34.8 us                                                    | 34.5 us: 1.01x faster                                                |
| json_loads                 | 28.9 us                                                    | 28.7 us: 1.01x faster                                                |
| meteor_contest             | 110 ms                                                     | 109 ms: 1.01x faster                                                 |
| coroutines                 | 23.2 ms                                                    | 23.0 ms: 1.01x faster                                                |
| pickle_list                | 5.11 us                                                    | 5.09 us: 1.00x faster                                                |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.00x slower                                                |
| sqlglot_parse              | 1.32 ms                                                    | 1.33 ms: 1.01x slower                                                |
| comprehensions             | 16.6 us                                                    | 16.7 us: 1.01x slower                                                |
| python_startup_no_site     | 7.11 ms                                                    | 7.17 ms: 1.01x slower                                                |
| tornado_http               | 94.6 ms                                                    | 95.7 ms: 1.01x slower                                                |
| 2to3                       | 274 ms                                                     | 278 ms: 1.01x slower                                                 |
| typing_runtime_protocols   | 165 us                                                     | 167 us: 1.01x slower                                                 |
| pickle                     | 11.5 us                                                    | 11.7 us: 1.02x slower                                                |
| sqlglot_transpile          | 1.63 ms                                                    | 1.67 ms: 1.02x slower                                                |
| sqlglot_normalize          | 110 ms                                                     | 113 ms: 1.02x slower                                                 |
| pycparser                  | 1.16 sec                                                   | 1.19 sec: 1.02x slower                                               |
| raytrace                   | 267 ms                                                     | 274 ms: 1.03x slower                                                 |
| genshi_text                | 23.7 ms                                                    | 24.5 ms: 1.03x slower                                                |
| async_generators           | 442 ms                                                     | 460 ms: 1.04x slower                                                 |
| django_template            | 34.8 ms                                                    | 36.6 ms: 1.05x slower                                                |
| sqlglot_optimize           | 55.5 ms                                                    | 58.4 ms: 1.05x slower                                                |
| dulwich_log                | 67.2 ms                                                    | 70.7 ms: 1.05x slower                                                |
| nqueens                    | 81.4 ms                                                    | 86.1 ms: 1.06x slower                                                |
| regex_compile              | 137 ms                                                     | 145 ms: 1.06x slower                                                 |
| docutils                   | 2.83 sec                                                   | 3.00 sec: 1.06x slower                                               |
| sympy_expand               | 473 ms                                                     | 507 ms: 1.07x slower                                                 |
| sympy_str                  | 282 ms                                                     | 304 ms: 1.08x slower                                                 |
| genshi_xml                 | 51.6 ms                                                    | 55.9 ms: 1.08x slower                                                |
| generators                 | 29.6 ms                                                    | 33.0 ms: 1.11x slower                                                |
| sympy_integrate            | 20.5 ms                                                    | 23.0 ms: 1.12x slower                                                |
| sympy_sum                  | 156 ms                                                     | 175 ms: 1.13x slower                                                 |
| pylint                     | 317 ms                                                     | 374 ms: 1.18x slower                                                 |
| hexiom                     | 6.30 ms                                                    | 7.73 ms: 1.23x slower                                                |
| Geometric mean             | (ref)                                                      | 1.04x faster                                                         |

Benchmark hidden because not significant (4): async_tree_io, json, bench_thread_pool, unpickle
Ignored benchmarks (7) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20240906-3.14.0a0-b1a2c42-JIT/bm-20240906-linux-x86_64-brandtbucher-trace_through-3.14.0a0-b1a2c42.json: unpack_sequence

# HPT report

- Reliability score: 99.98% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.09x