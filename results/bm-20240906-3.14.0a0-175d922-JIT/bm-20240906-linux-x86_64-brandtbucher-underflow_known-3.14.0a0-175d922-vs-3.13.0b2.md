# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: underflow_known
- machine: linux-x86_64
- commit hash: 175d922
- commit date: 2024-09-06
- overall geometric mean: 1.05x faster
- HPT reliability: 99.93%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240906-linux-x86_64-brandtbucher-underflow_known-3.14.0a0-175d922 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 276 ms: 1.01x slower                                                   |
| docutils       | 2.83 sec                                                   | 3.01 sec: 1.07x slower                                                 |
| html5lib       | 67.2 ms                                                    | 64.8 ms: 1.04x faster                                                  |
| tornado_http   | 94.6 ms                                                    | 97.0 ms: 1.02x slower                                                  |
| Geometric mean | (ref)                                                      | 1.01x slower                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240906-linux-x86_64-brandtbucher-underflow_known-3.14.0a0-175d922 |
|----------------------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_none            | 378 ms                                                     | 326 ms: 1.16x faster                                                   |
| async_tree_memoization     | 463 ms                                                     | 401 ms: 1.16x faster                                                   |
| async_tree_memoization_tg  | 444 ms                                                     | 405 ms: 1.10x faster                                                   |
| async_tree_none_tg         | 336 ms                                                     | 309 ms: 1.09x faster                                                   |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 567 ms: 1.08x faster                                                   |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 548 ms: 1.07x faster                                                   |
| async_tree_io_tg           | 936 ms                                                     | 898 ms: 1.04x faster                                                   |
| Geometric mean             | (ref)                                                      | 1.09x faster                                                           |

Benchmark hidden because not significant (1): async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240906-linux-x86_64-brandtbucher-underflow_known-3.14.0a0-175d922 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 78.9 ms                                                    | 70.3 ms: 1.12x faster                                                  |
| nbody          | 88.3 ms                                                    | 79.5 ms: 1.11x faster                                                  |
| pidigits       | 191 ms                                                     | 187 ms: 1.02x faster                                                   |
| Geometric mean | (ref)                                                      | 1.08x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240906-linux-x86_64-brandtbucher-underflow_known-3.14.0a0-175d922 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_v8       | 25.1 ms                                                    | 24.7 ms: 1.02x faster                                                  |
| regex_dna      | 221 ms                                                     | 221 ms: 1.00x faster                                                   |
| regex_effbot   | 3.67 ms                                                    | 3.71 ms: 1.01x slower                                                  |
| regex_compile  | 137 ms                                                     | 142 ms: 1.04x slower                                                   |
| Geometric mean | (ref)                                                      | 1.01x slower                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240906-linux-x86_64-brandtbucher-underflow_known-3.14.0a0-175d922 |
|----------------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| xml_etree_generate   | 87.4 ms                                                    | 77.8 ms: 1.12x faster                                                  |
| xml_etree_parse      | 162 ms                                                     | 146 ms: 1.11x faster                                                   |
| xml_etree_process    | 61.2 ms                                                    | 55.3 ms: 1.11x faster                                                  |
| tomli_loads          | 2.12 sec                                                   | 1.92 sec: 1.10x faster                                                 |
| unpickle_pure_python | 218 us                                                     | 199 us: 1.10x faster                                                   |
| xml_etree_iterparse  | 107 ms                                                     | 98.6 ms: 1.09x faster                                                  |
| json_dumps           | 10.7 ms                                                    | 10.3 ms: 1.04x faster                                                  |
| unpickle_list        | 5.34 us                                                    | 5.16 us: 1.04x faster                                                  |
| json_loads           | 28.9 us                                                    | 28.2 us: 1.02x faster                                                  |
| pickle_pure_python   | 305 us                                                     | 300 us: 1.02x faster                                                   |
| pickle_dict          | 34.8 us                                                    | 34.9 us: 1.00x slower                                                  |
| pickle               | 11.5 us                                                    | 11.6 us: 1.01x slower                                                  |
| pickle_list          | 5.11 us                                                    | 5.18 us: 1.01x slower                                                  |
| Geometric mean       | (ref)                                                      | 1.05x faster                                                           |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240906-linux-x86_64-brandtbucher-underflow_known-3.14.0a0-175d922 |
|------------------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.6 ms: 1.01x faster                                                  |
| python_startup_no_site | 7.11 ms                                                    | 7.16 ms: 1.01x slower                                                  |
| Geometric mean         | (ref)                                                      | 1.00x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240906-linux-x86_64-brandtbucher-underflow_known-3.14.0a0-175d922 |
|-----------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 9.81 ms: 1.15x faster                                                  |
| genshi_text     | 23.7 ms                                                    | 24.3 ms: 1.03x slower                                                  |
| django_template | 34.8 ms                                                    | 36.2 ms: 1.04x slower                                                  |
| genshi_xml      | 51.6 ms                                                    | 57.3 ms: 1.11x slower                                                  |
| Geometric mean  | (ref)                                                      | 1.01x slower                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240906-linux-x86_64-brandtbucher-underflow_known-3.14.0a0-175d922 |
|----------------------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| deepcopy_memo              | 39.7 us                                                    | 26.0 us: 1.53x faster                                                  |
| deepcopy                   | 367 us                                                     | 264 us: 1.39x faster                                                   |
| richards_super             | 57.4 ms                                                    | 42.6 ms: 1.35x faster                                                  |
| scimark_fft                | 392 ms                                                     | 305 ms: 1.29x faster                                                   |
| richards                   | 50.9 ms                                                    | 40.0 ms: 1.27x faster                                                  |
| deepcopy_reduce            | 3.35 us                                                    | 2.64 us: 1.27x faster                                                  |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.23 ms: 1.25x faster                                                  |
| spectral_norm              | 116 ms                                                     | 99.7 ms: 1.16x faster                                                  |
| async_tree_none            | 378 ms                                                     | 326 ms: 1.16x faster                                                   |
| crypto_pyaes               | 77.5 ms                                                    | 66.9 ms: 1.16x faster                                                  |
| async_tree_memoization     | 463 ms                                                     | 401 ms: 1.16x faster                                                   |
| mako                       | 11.2 ms                                                    | 9.81 ms: 1.15x faster                                                  |
| bpe_tokeniser              | 5.02 sec                                                   | 4.42 sec: 1.14x faster                                                 |
| xml_etree_generate         | 87.4 ms                                                    | 77.8 ms: 1.12x faster                                                  |
| float                      | 78.9 ms                                                    | 70.3 ms: 1.12x faster                                                  |
| scimark_lu                 | 122 ms                                                     | 109 ms: 1.12x faster                                                   |
| nbody                      | 88.3 ms                                                    | 79.5 ms: 1.11x faster                                                  |
| logging_silent             | 105 ns                                                     | 94.5 ns: 1.11x faster                                                  |
| scimark_sor                | 127 ms                                                     | 115 ms: 1.11x faster                                                   |
| xml_etree_parse            | 162 ms                                                     | 146 ms: 1.11x faster                                                   |
| xml_etree_process          | 61.2 ms                                                    | 55.3 ms: 1.11x faster                                                  |
| tomli_loads                | 2.12 sec                                                   | 1.92 sec: 1.10x faster                                                 |
| go                         | 145 ms                                                     | 132 ms: 1.10x faster                                                   |
| mdp                        | 2.79 sec                                                   | 2.54 sec: 1.10x faster                                                 |
| unpickle_pure_python       | 218 us                                                     | 199 us: 1.10x faster                                                   |
| async_tree_memoization_tg  | 444 ms                                                     | 405 ms: 1.10x faster                                                   |
| xml_etree_iterparse        | 107 ms                                                     | 98.6 ms: 1.09x faster                                                  |
| gc_traversal               | 3.98 ms                                                    | 3.66 ms: 1.09x faster                                                  |
| async_tree_none_tg         | 336 ms                                                     | 309 ms: 1.09x faster                                                   |
| pathlib                    | 17.3 ms                                                    | 16.0 ms: 1.09x faster                                                  |
| coverage                   | 93.1 ms                                                    | 86.0 ms: 1.08x faster                                                  |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 567 ms: 1.08x faster                                                   |
| pyflate                    | 484 ms                                                     | 450 ms: 1.08x faster                                                   |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 548 ms: 1.07x faster                                                   |
| sqlite_synth               | 2.99 us                                                    | 2.79 us: 1.07x faster                                                  |
| fannkuch                   | 402 ms                                                     | 376 ms: 1.07x faster                                                   |
| thrift                     | 823 us                                                     | 778 us: 1.06x faster                                                   |
| telco                      | 8.41 ms                                                    | 7.97 ms: 1.06x faster                                                  |
| pprint_safe_repr           | 758 ms                                                     | 724 ms: 1.05x faster                                                   |
| logging_format             | 6.47 us                                                    | 6.19 us: 1.05x faster                                                  |
| async_tree_io_tg           | 936 ms                                                     | 898 ms: 1.04x faster                                                   |
| html5lib                   | 67.2 ms                                                    | 64.8 ms: 1.04x faster                                                  |
| json_dumps                 | 10.7 ms                                                    | 10.3 ms: 1.04x faster                                                  |
| unpickle_list              | 5.34 us                                                    | 5.16 us: 1.04x faster                                                  |
| pprint_pformat             | 1.56 sec                                                   | 1.51 sec: 1.03x faster                                                 |
| meteor_contest             | 110 ms                                                     | 107 ms: 1.03x faster                                                   |
| chaos                      | 61.3 ms                                                    | 59.7 ms: 1.03x faster                                                  |
| asyncio_tcp                | 508 ms                                                     | 495 ms: 1.03x faster                                                   |
| create_gc_cycles           | 1.82 ms                                                    | 1.77 ms: 1.03x faster                                                  |
| json_loads                 | 28.9 us                                                    | 28.2 us: 1.02x faster                                                  |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.80 sec: 1.02x faster                                                 |
| pidigits                   | 191 ms                                                     | 187 ms: 1.02x faster                                                   |
| scimark_monte_carlo        | 69.2 ms                                                    | 67.8 ms: 1.02x faster                                                  |
| asyncio_websockets         | 567 ms                                                     | 556 ms: 1.02x faster                                                   |
| logging_simple             | 5.74 us                                                    | 5.64 us: 1.02x faster                                                  |
| pickle_pure_python         | 305 us                                                     | 300 us: 1.02x faster                                                   |
| regex_v8                   | 25.1 ms                                                    | 24.7 ms: 1.02x faster                                                  |
| python_startup             | 10.8 ms                                                    | 10.6 ms: 1.01x faster                                                  |
| deltablue                  | 3.25 ms                                                    | 3.22 ms: 1.01x faster                                                  |
| coroutines                 | 23.2 ms                                                    | 23.0 ms: 1.01x faster                                                  |
| comprehensions             | 16.6 us                                                    | 16.5 us: 1.01x faster                                                  |
| regex_dna                  | 221 ms                                                     | 221 ms: 1.00x faster                                                   |
| pickle_dict                | 34.8 us                                                    | 34.9 us: 1.00x slower                                                  |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                                  |
| python_startup_no_site     | 7.11 ms                                                    | 7.16 ms: 1.01x slower                                                  |
| 2to3                       | 274 ms                                                     | 276 ms: 1.01x slower                                                   |
| bench_thread_pool          | 834 us                                                     | 842 us: 1.01x slower                                                   |
| regex_effbot               | 3.67 ms                                                    | 3.71 ms: 1.01x slower                                                  |
| pickle                     | 11.5 us                                                    | 11.6 us: 1.01x slower                                                  |
| pickle_list                | 5.11 us                                                    | 5.18 us: 1.01x slower                                                  |
| sqlglot_normalize          | 110 ms                                                     | 112 ms: 1.02x slower                                                   |
| dulwich_log                | 67.2 ms                                                    | 68.5 ms: 1.02x slower                                                  |
| raytrace                   | 267 ms                                                     | 272 ms: 1.02x slower                                                   |
| tornado_http               | 94.6 ms                                                    | 97.0 ms: 1.02x slower                                                  |
| genshi_text                | 23.7 ms                                                    | 24.3 ms: 1.03x slower                                                  |
| sqlglot_parse              | 1.32 ms                                                    | 1.37 ms: 1.04x slower                                                  |
| django_template            | 34.8 ms                                                    | 36.2 ms: 1.04x slower                                                  |
| async_generators           | 442 ms                                                     | 460 ms: 1.04x slower                                                   |
| regex_compile              | 137 ms                                                     | 142 ms: 1.04x slower                                                   |
| pycparser                  | 1.16 sec                                                   | 1.21 sec: 1.05x slower                                                 |
| sqlglot_transpile          | 1.63 ms                                                    | 1.71 ms: 1.05x slower                                                  |
| nqueens                    | 81.4 ms                                                    | 85.2 ms: 1.05x slower                                                  |
| sqlglot_optimize           | 55.5 ms                                                    | 58.3 ms: 1.05x slower                                                  |
| sympy_str                  | 282 ms                                                     | 299 ms: 1.06x slower                                                   |
| docutils                   | 2.83 sec                                                   | 3.01 sec: 1.07x slower                                                 |
| sympy_expand               | 473 ms                                                     | 507 ms: 1.07x slower                                                   |
| hexiom                     | 6.30 ms                                                    | 6.88 ms: 1.09x slower                                                  |
| sympy_sum                  | 156 ms                                                     | 172 ms: 1.11x slower                                                   |
| genshi_xml                 | 51.6 ms                                                    | 57.3 ms: 1.11x slower                                                  |
| sympy_integrate            | 20.5 ms                                                    | 22.8 ms: 1.11x slower                                                  |
| generators                 | 29.6 ms                                                    | 33.3 ms: 1.12x slower                                                  |
| pylint                     | 317 ms                                                     | 372 ms: 1.17x slower                                                   |
| Geometric mean             | (ref)                                                      | 1.05x faster                                                           |

Benchmark hidden because not significant (4): unpickle, async_tree_io, json, typing_runtime_protocols
Ignored benchmarks (7) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20240906-3.14.0a0-175d922-JIT/bm-20240906-linux-x86_64-brandtbucher-underflow_known-3.14.0a0-175d922.json: unpack_sequence

# HPT report

- Reliability score: 99.93% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.09x