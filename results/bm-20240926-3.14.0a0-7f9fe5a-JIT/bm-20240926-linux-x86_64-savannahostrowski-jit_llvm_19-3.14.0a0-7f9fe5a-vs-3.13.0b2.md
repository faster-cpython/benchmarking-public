# Results vs. 3.13.0b2

- fork: savannahostrowski
- ref: jit_llvm_19
- machine: linux-x86_64
- commit hash: 7f9fe5a
- commit date: 2024-09-26
- overall geometric mean: 1.05x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240926-linux-x86_64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| docutils       | 2.83 sec                                                   | 2.94 sec: 1.04x slower                                                  |
| html5lib       | 67.2 ms                                                    | 62.0 ms: 1.08x faster                                                   |
| Geometric mean | (ref)                                                      | 1.01x faster                                                            |

Benchmark hidden because not significant (2): 2to3, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240926-linux-x86_64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none            | 378 ms                                                     | 315 ms: 1.20x faster                                                    |
| async_tree_memoization     | 463 ms                                                     | 397 ms: 1.17x faster                                                    |
| async_tree_memoization_tg  | 444 ms                                                     | 388 ms: 1.14x faster                                                    |
| async_tree_none_tg         | 336 ms                                                     | 308 ms: 1.09x faster                                                    |
| async_tree_io_tg           | 936 ms                                                     | 875 ms: 1.07x faster                                                    |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 572 ms: 1.07x faster                                                    |
| async_tree_io              | 939 ms                                                     | 885 ms: 1.06x faster                                                    |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 556 ms: 1.06x faster                                                    |
| Geometric mean             | (ref)                                                      | 1.11x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240926-linux-x86_64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 78.9 ms                                                    | 70.1 ms: 1.13x faster                                                   |
| nbody          | 88.3 ms                                                    | 81.8 ms: 1.08x faster                                                   |
| pidigits       | 191 ms                                                     | 186 ms: 1.03x faster                                                    |
| Geometric mean | (ref)                                                      | 1.08x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240926-linux-x86_64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_dna      | 221 ms                                                     | 212 ms: 1.04x faster                                                    |
| regex_v8       | 25.1 ms                                                    | 24.2 ms: 1.04x faster                                                   |
| regex_effbot   | 3.67 ms                                                    | 3.72 ms: 1.01x slower                                                   |
| regex_compile  | 137 ms                                                     | 142 ms: 1.04x slower                                                    |
| Geometric mean | (ref)                                                      | 1.01x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240926-linux-x86_64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_generate   | 87.4 ms                                                    | 78.1 ms: 1.12x faster                                                   |
| xml_etree_process    | 61.2 ms                                                    | 55.0 ms: 1.11x faster                                                   |
| xml_etree_parse      | 162 ms                                                     | 147 ms: 1.10x faster                                                    |
| xml_etree_iterparse  | 107 ms                                                     | 98.6 ms: 1.09x faster                                                   |
| tomli_loads          | 2.12 sec                                                   | 1.96 sec: 1.08x faster                                                  |
| json_dumps           | 10.7 ms                                                    | 10.1 ms: 1.06x faster                                                   |
| json_loads           | 28.9 us                                                    | 27.2 us: 1.06x faster                                                   |
| pickle_dict          | 34.8 us                                                    | 33.3 us: 1.05x faster                                                   |
| unpickle             | 15.1 us                                                    | 14.7 us: 1.03x faster                                                   |
| unpickle_pure_python | 218 us                                                     | 215 us: 1.02x faster                                                    |
| unpickle_list        | 5.34 us                                                    | 5.30 us: 1.01x faster                                                   |
| pickle_pure_python   | 305 us                                                     | 307 us: 1.01x slower                                                    |
| pickle               | 11.5 us                                                    | 11.6 us: 1.01x slower                                                   |
| pickle_list          | 5.11 us                                                    | 5.20 us: 1.02x slower                                                   |
| Geometric mean       | (ref)                                                      | 1.05x faster                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240926-linux-x86_64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|------------------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                                   |
| python_startup_no_site | 7.11 ms                                                    | 7.08 ms: 1.00x faster                                                   |
| Geometric mean         | (ref)                                                      | 1.01x faster                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240926-linux-x86_64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|-----------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 10.1 ms: 1.11x faster                                                   |
| django_template | 34.8 ms                                                    | 35.5 ms: 1.02x slower                                                   |
| genshi_text     | 23.7 ms                                                    | 24.4 ms: 1.03x slower                                                   |
| genshi_xml      | 51.6 ms                                                    | 57.2 ms: 1.11x slower                                                   |
| Geometric mean  | (ref)                                                      | 1.01x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240926-linux-x86_64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy_memo              | 39.7 us                                                    | 26.7 us: 1.49x faster                                                   |
| deepcopy                   | 367 us                                                     | 261 us: 1.40x faster                                                    |
| richards_super             | 57.4 ms                                                    | 44.9 ms: 1.28x faster                                                   |
| richards                   | 50.9 ms                                                    | 39.8 ms: 1.28x faster                                                   |
| deepcopy_reduce            | 3.35 us                                                    | 2.65 us: 1.27x faster                                                   |
| scimark_fft                | 392 ms                                                     | 312 ms: 1.26x faster                                                    |
| async_tree_none            | 378 ms                                                     | 315 ms: 1.20x faster                                                    |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.39 ms: 1.20x faster                                                   |
| async_tree_memoization     | 463 ms                                                     | 397 ms: 1.17x faster                                                    |
| crypto_pyaes               | 77.5 ms                                                    | 66.8 ms: 1.16x faster                                                   |
| spectral_norm              | 116 ms                                                     | 101 ms: 1.15x faster                                                    |
| async_tree_memoization_tg  | 444 ms                                                     | 388 ms: 1.14x faster                                                    |
| bpe_tokeniser              | 5.02 sec                                                   | 4.45 sec: 1.13x faster                                                  |
| float                      | 78.9 ms                                                    | 70.1 ms: 1.13x faster                                                   |
| xml_etree_generate         | 87.4 ms                                                    | 78.1 ms: 1.12x faster                                                   |
| scimark_lu                 | 122 ms                                                     | 109 ms: 1.11x faster                                                    |
| xml_etree_process          | 61.2 ms                                                    | 55.0 ms: 1.11x faster                                                   |
| mako                       | 11.2 ms                                                    | 10.1 ms: 1.11x faster                                                   |
| xml_etree_parse            | 162 ms                                                     | 147 ms: 1.10x faster                                                    |
| scimark_monte_carlo        | 69.2 ms                                                    | 62.8 ms: 1.10x faster                                                   |
| go                         | 145 ms                                                     | 132 ms: 1.10x faster                                                    |
| coverage                   | 93.1 ms                                                    | 84.8 ms: 1.10x faster                                                   |
| sqlite_synth               | 2.99 us                                                    | 2.74 us: 1.09x faster                                                   |
| scimark_sor                | 127 ms                                                     | 117 ms: 1.09x faster                                                    |
| async_tree_none_tg         | 336 ms                                                     | 308 ms: 1.09x faster                                                    |
| xml_etree_iterparse        | 107 ms                                                     | 98.6 ms: 1.09x faster                                                   |
| pathlib                    | 17.3 ms                                                    | 15.9 ms: 1.09x faster                                                   |
| html5lib                   | 67.2 ms                                                    | 62.0 ms: 1.08x faster                                                   |
| tomli_loads                | 2.12 sec                                                   | 1.96 sec: 1.08x faster                                                  |
| nbody                      | 88.3 ms                                                    | 81.8 ms: 1.08x faster                                                   |
| mdp                        | 2.79 sec                                                   | 2.60 sec: 1.07x faster                                                  |
| telco                      | 8.41 ms                                                    | 7.86 ms: 1.07x faster                                                   |
| async_tree_io_tg           | 936 ms                                                     | 875 ms: 1.07x faster                                                    |
| logging_format             | 6.47 us                                                    | 6.05 us: 1.07x faster                                                   |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 572 ms: 1.07x faster                                                    |
| json_dumps                 | 10.7 ms                                                    | 10.1 ms: 1.06x faster                                                   |
| json_loads                 | 28.9 us                                                    | 27.2 us: 1.06x faster                                                   |
| async_tree_io              | 939 ms                                                     | 885 ms: 1.06x faster                                                    |
| pyflate                    | 484 ms                                                     | 458 ms: 1.06x faster                                                    |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 556 ms: 1.06x faster                                                    |
| fannkuch                   | 402 ms                                                     | 384 ms: 1.05x faster                                                    |
| thrift                     | 823 us                                                     | 787 us: 1.05x faster                                                    |
| pickle_dict                | 34.8 us                                                    | 33.3 us: 1.05x faster                                                   |
| regex_dna                  | 221 ms                                                     | 212 ms: 1.04x faster                                                    |
| regex_v8                   | 25.1 ms                                                    | 24.2 ms: 1.04x faster                                                   |
| json                       | 5.31 ms                                                    | 5.11 ms: 1.04x faster                                                   |
| asyncio_tcp                | 508 ms                                                     | 491 ms: 1.03x faster                                                    |
| create_gc_cycles           | 1.82 ms                                                    | 1.76 ms: 1.03x faster                                                   |
| unpickle                   | 15.1 us                                                    | 14.7 us: 1.03x faster                                                   |
| logging_simple             | 5.74 us                                                    | 5.58 us: 1.03x faster                                                   |
| pidigits                   | 191 ms                                                     | 186 ms: 1.03x faster                                                    |
| chaos                      | 61.3 ms                                                    | 59.7 ms: 1.03x faster                                                   |
| meteor_contest             | 110 ms                                                     | 107 ms: 1.02x faster                                                    |
| asyncio_websockets         | 567 ms                                                     | 556 ms: 1.02x faster                                                    |
| deltablue                  | 3.25 ms                                                    | 3.19 ms: 1.02x faster                                                   |
| python_startup             | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                                   |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.81 sec: 1.02x faster                                                  |
| typing_runtime_protocols   | 165 us                                                     | 162 us: 1.02x faster                                                    |
| unpickle_pure_python       | 218 us                                                     | 215 us: 1.02x faster                                                    |
| comprehensions             | 16.6 us                                                    | 16.4 us: 1.01x faster                                                   |
| pprint_pformat             | 1.56 sec                                                   | 1.54 sec: 1.01x faster                                                  |
| unpickle_list              | 5.34 us                                                    | 5.30 us: 1.01x faster                                                   |
| coroutines                 | 23.2 ms                                                    | 23.0 ms: 1.01x faster                                                   |
| python_startup_no_site     | 7.11 ms                                                    | 7.08 ms: 1.00x faster                                                   |
| pickle_pure_python         | 305 us                                                     | 307 us: 1.01x slower                                                    |
| sqlglot_parse              | 1.32 ms                                                    | 1.33 ms: 1.01x slower                                                   |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                                   |
| bench_thread_pool          | 834 us                                                     | 841 us: 1.01x slower                                                    |
| dulwich_log                | 67.2 ms                                                    | 67.9 ms: 1.01x slower                                                   |
| pickle                     | 11.5 us                                                    | 11.6 us: 1.01x slower                                                   |
| regex_effbot               | 3.67 ms                                                    | 3.72 ms: 1.01x slower                                                   |
| sqlglot_normalize          | 110 ms                                                     | 112 ms: 1.01x slower                                                    |
| pickle_list                | 5.11 us                                                    | 5.20 us: 1.02x slower                                                   |
| pprint_safe_repr           | 758 ms                                                     | 772 ms: 1.02x slower                                                    |
| django_template            | 34.8 ms                                                    | 35.5 ms: 1.02x slower                                                   |
| sqlglot_transpile          | 1.63 ms                                                    | 1.67 ms: 1.02x slower                                                   |
| async_generators           | 442 ms                                                     | 455 ms: 1.03x slower                                                    |
| genshi_text                | 23.7 ms                                                    | 24.4 ms: 1.03x slower                                                   |
| raytrace                   | 267 ms                                                     | 276 ms: 1.04x slower                                                    |
| sqlglot_optimize           | 55.5 ms                                                    | 57.7 ms: 1.04x slower                                                   |
| docutils                   | 2.83 sec                                                   | 2.94 sec: 1.04x slower                                                  |
| regex_compile              | 137 ms                                                     | 142 ms: 1.04x slower                                                    |
| nqueens                    | 81.4 ms                                                    | 85.6 ms: 1.05x slower                                                   |
| sympy_str                  | 282 ms                                                     | 298 ms: 1.05x slower                                                    |
| sympy_expand               | 473 ms                                                     | 502 ms: 1.06x slower                                                    |
| hexiom                     | 6.30 ms                                                    | 6.87 ms: 1.09x slower                                                   |
| sympy_sum                  | 156 ms                                                     | 172 ms: 1.10x slower                                                    |
| sympy_integrate            | 20.5 ms                                                    | 22.7 ms: 1.11x slower                                                   |
| genshi_xml                 | 51.6 ms                                                    | 57.2 ms: 1.11x slower                                                   |
| generators                 | 29.6 ms                                                    | 33.1 ms: 1.12x slower                                                   |
| pylint                     | 317 ms                                                     | 370 ms: 1.17x slower                                                    |
| Geometric mean             | (ref)                                                      | 1.05x faster                                                            |

Benchmark hidden because not significant (5): logging_silent, gc_traversal, tornado_http, 2to3, pycparser
Ignored benchmarks (7) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20240926-3.14.0a0-7f9fe5a-JIT/bm-20240926-linux-x86_64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a.json: unpack_sequence

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.08x