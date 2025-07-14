# Results vs. base

- fork: python
- ref: 47b01da4ccedd9c00fad
- machine: linux-x86_64
- commit hash: 47b01da
- commit date: 2025-07-12
- overall geometric mean: 1.009x faster
- HPT reliability: 70.04%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20250712-3.15.0a0-47b01da/bm-20250712-pythonperf2-x86_64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da.json | results/bm-20250712-3.15.0a0-47b01da-JIT/bm-20250712-pythonperf2-x86_64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da.json |
|----------------|:---------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 281 ms                                                                                                                | 285 ms: 1.02x slower                                                                                                      |
| docutils       | 2.86 sec                                                                                                              | 2.91 sec: 1.02x slower                                                                                                    |
| html5lib       | 65.5 ms                                                                                                               | 67.6 ms: 1.03x slower                                                                                                     |
| Geometric mean | (ref)                                                                                                                 | 1.02x slower                                                                                                              |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | results/bm-20250712-3.15.0a0-47b01da/bm-20250712-pythonperf2-x86_64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da.json | results/bm-20250712-3.15.0a0-47b01da-JIT/bm-20250712-pythonperf2-x86_64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da.json |
|-------------------------|:---------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| async_tree_io_tg        | 638 ms                                                                                                                | 629 ms: 1.01x faster                                                                                                      |
| async_tree_cpu_io_mixed | 505 ms                                                                                                                | 502 ms: 1.01x faster                                                                                                      |
| coroutines              | 22.3 ms                                                                                                               | 22.5 ms: 1.01x slower                                                                                                     |
| async_tree_none         | 273 ms                                                                                                                | 276 ms: 1.01x slower                                                                                                      |
| asyncio_tcp             | 364 ms                                                                                                                | 372 ms: 1.02x slower                                                                                                      |
| async_generators        | 422 ms                                                                                                                | 443 ms: 1.05x slower                                                                                                      |
| Geometric mean          | (ref)                                                                                                                 | 1.01x slower                                                                                                              |

Benchmark hidden because not significant (7): async_tree_io, async_tree_cpu_io_mixed_tg, asyncio_tcp_ssl, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20250712-3.15.0a0-47b01da/bm-20250712-pythonperf2-x86_64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da.json | results/bm-20250712-3.15.0a0-47b01da-JIT/bm-20250712-pythonperf2-x86_64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da.json |
|----------------|:---------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| float          | 70.8 ms                                                                                                               | 63.5 ms: 1.12x faster                                                                                                     |
| pidigits       | 256 ms                                                                                                                | 256 ms: 1.00x faster                                                                                                      |
| nbody          | 93.0 ms                                                                                                               | 98.2 ms: 1.06x slower                                                                                                     |
| Geometric mean | (ref)                                                                                                                 | 1.02x faster                                                                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20250712-3.15.0a0-47b01da/bm-20250712-pythonperf2-x86_64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da.json | results/bm-20250712-3.15.0a0-47b01da-JIT/bm-20250712-pythonperf2-x86_64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da.json |
|----------------|:---------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| regex_dna      | 229 ms                                                                                                                | 225 ms: 1.01x faster                                                                                                      |
| regex_compile  | 133 ms                                                                                                                | 131 ms: 1.01x faster                                                                                                      |
| regex_effbot   | 3.56 ms                                                                                                               | 3.57 ms: 1.00x slower                                                                                                     |
| regex_v8       | 23.3 ms                                                                                                               | 24.1 ms: 1.03x slower                                                                                                     |
| Geometric mean | (ref)                                                                                                                 | 1.00x slower                                                                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20250712-3.15.0a0-47b01da/bm-20250712-pythonperf2-x86_64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da.json | results/bm-20250712-3.15.0a0-47b01da-JIT/bm-20250712-pythonperf2-x86_64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da.json |
|----------------------|:---------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| pickle_dict          | 36.6 us                                                                                                               | 33.5 us: 1.09x faster                                                                                                     |
| xml_etree_process    | 59.3 ms                                                                                                               | 55.5 ms: 1.07x faster                                                                                                     |
| tomli_loads          | 2.02 sec                                                                                                              | 1.91 sec: 1.06x faster                                                                                                    |
| unpickle_pure_python | 206 us                                                                                                                | 196 us: 1.05x faster                                                                                                      |
| pickle               | 12.7 us                                                                                                               | 12.2 us: 1.04x faster                                                                                                     |
| xml_etree_generate   | 81.9 ms                                                                                                               | 80.1 ms: 1.02x faster                                                                                                     |
| pickle_list          | 5.03 us                                                                                                               | 5.00 us: 1.01x faster                                                                                                     |
| xml_etree_parse      | 139 ms                                                                                                                | 139 ms: 1.01x faster                                                                                                      |
| json_loads           | 25.6 us                                                                                                               | 25.5 us: 1.01x faster                                                                                                     |
| xml_etree_iterparse  | 97.4 ms                                                                                                               | 97.7 ms: 1.00x slower                                                                                                     |
| pickle_pure_python   | 333 us                                                                                                                | 335 us: 1.01x slower                                                                                                      |
| unpickle_list        | 5.02 us                                                                                                               | 5.05 us: 1.01x slower                                                                                                     |
| unpickle             | 14.8 us                                                                                                               | 14.9 us: 1.01x slower                                                                                                     |
| Geometric mean       | (ref)                                                                                                                 | 1.02x faster                                                                                                              |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20250712-3.15.0a0-47b01da/bm-20250712-pythonperf2-x86_64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da.json | results/bm-20250712-3.15.0a0-47b01da-JIT/bm-20250712-pythonperf2-x86_64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da.json |
|------------------------|:---------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| python_startup         | 15.3 ms                                                                                                               | 15.3 ms: 1.00x slower                                                                                                     |
| python_startup_no_site | 8.83 ms                                                                                                               | 8.86 ms: 1.00x slower                                                                                                     |
| Geometric mean         | (ref)                                                                                                                 | 1.00x slower                                                                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark      | results/bm-20250712-3.15.0a0-47b01da/bm-20250712-pythonperf2-x86_64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da.json | results/bm-20250712-3.15.0a0-47b01da-JIT/bm-20250712-pythonperf2-x86_64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da.json |
|----------------|:---------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| mako           | 10.8 ms                                                                                                               | 9.73 ms: 1.11x faster                                                                                                     |
| genshi_text    | 23.2 ms                                                                                                               | 22.7 ms: 1.02x faster                                                                                                     |
| genshi_xml     | 52.8 ms                                                                                                               | 53.8 ms: 1.02x slower                                                                                                     |
| Geometric mean | (ref)                                                                                                                 | 1.03x faster                                                                                                              |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                | results/bm-20250712-3.15.0a0-47b01da/bm-20250712-pythonperf2-x86_64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da.json | results/bm-20250712-3.15.0a0-47b01da-JIT/bm-20250712-pythonperf2-x86_64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da.json |
|--------------------------|:---------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| richards                 | 45.6 ms                                                                                                               | 35.2 ms: 1.29x faster                                                                                                     |
| richards_super           | 51.8 ms                                                                                                               | 40.5 ms: 1.28x faster                                                                                                     |
| deepcopy_memo            | 28.8 us                                                                                                               | 25.9 us: 1.12x faster                                                                                                     |
| float                    | 70.8 ms                                                                                                               | 63.5 ms: 1.12x faster                                                                                                     |
| deltablue                | 3.20 ms                                                                                                               | 2.88 ms: 1.11x faster                                                                                                     |
| mako                     | 10.8 ms                                                                                                               | 9.73 ms: 1.11x faster                                                                                                     |
| spectral_norm            | 86.8 ms                                                                                                               | 78.3 ms: 1.11x faster                                                                                                     |
| pickle_dict              | 36.6 us                                                                                                               | 33.5 us: 1.09x faster                                                                                                     |
| xml_etree_process        | 59.3 ms                                                                                                               | 55.5 ms: 1.07x faster                                                                                                     |
| tomli_loads              | 2.02 sec                                                                                                              | 1.91 sec: 1.06x faster                                                                                                    |
| unpickle_pure_python     | 206 us                                                                                                                | 196 us: 1.05x faster                                                                                                      |
| pprint_pformat           | 1.58 sec                                                                                                              | 1.50 sec: 1.05x faster                                                                                                    |
| scimark_fft              | 311 ms                                                                                                                | 297 ms: 1.05x faster                                                                                                      |
| pprint_safe_repr         | 775 ms                                                                                                                | 744 ms: 1.04x faster                                                                                                      |
| pickle                   | 12.7 us                                                                                                               | 12.2 us: 1.04x faster                                                                                                     |
| connected_components     | 423 ms                                                                                                                | 407 ms: 1.04x faster                                                                                                      |
| coverage                 | 84.4 ms                                                                                                               | 81.2 ms: 1.04x faster                                                                                                     |
| k_core                   | 2.09 sec                                                                                                              | 2.02 sec: 1.03x faster                                                                                                    |
| thrift                   | 856 us                                                                                                                | 831 us: 1.03x faster                                                                                                      |
| xml_etree_generate       | 81.9 ms                                                                                                               | 80.1 ms: 1.02x faster                                                                                                     |
| genshi_text              | 23.2 ms                                                                                                               | 22.7 ms: 1.02x faster                                                                                                     |
| bpe_tokeniser            | 4.73 sec                                                                                                              | 4.64 sec: 1.02x faster                                                                                                    |
| shortest_path            | 451 ms                                                                                                                | 443 ms: 1.02x faster                                                                                                      |
| pyflate                  | 427 ms                                                                                                                | 419 ms: 1.02x faster                                                                                                      |
| json                     | 5.38 ms                                                                                                               | 5.30 ms: 1.02x faster                                                                                                     |
| async_tree_io_tg         | 638 ms                                                                                                                | 629 ms: 1.01x faster                                                                                                      |
| regex_dna                | 229 ms                                                                                                                | 225 ms: 1.01x faster                                                                                                      |
| generators               | 29.5 ms                                                                                                               | 29.1 ms: 1.01x faster                                                                                                     |
| scimark_sor              | 105 ms                                                                                                                | 104 ms: 1.01x faster                                                                                                      |
| regex_compile            | 133 ms                                                                                                                | 131 ms: 1.01x faster                                                                                                      |
| pathlib                  | 17.1 ms                                                                                                               | 16.9 ms: 1.01x faster                                                                                                     |
| logging_silent           | 94.1 ns                                                                                                               | 93.2 ns: 1.01x faster                                                                                                     |
| sqlite_synth             | 2.84 us                                                                                                               | 2.81 us: 1.01x faster                                                                                                     |
| scimark_lu               | 96.6 ms                                                                                                               | 95.8 ms: 1.01x faster                                                                                                     |
| pickle_list              | 5.03 us                                                                                                               | 5.00 us: 1.01x faster                                                                                                     |
| xml_etree_parse          | 139 ms                                                                                                                | 139 ms: 1.01x faster                                                                                                      |
| subparsers               | 25.0 ms                                                                                                               | 24.9 ms: 1.01x faster                                                                                                     |
| json_loads               | 25.6 us                                                                                                               | 25.5 us: 1.01x faster                                                                                                     |
| async_tree_cpu_io_mixed  | 505 ms                                                                                                                | 502 ms: 1.01x faster                                                                                                      |
| pidigits                 | 256 ms                                                                                                                | 256 ms: 1.00x faster                                                                                                      |
| regex_effbot             | 3.56 ms                                                                                                               | 3.57 ms: 1.00x slower                                                                                                     |
| python_startup           | 15.3 ms                                                                                                               | 15.3 ms: 1.00x slower                                                                                                     |
| xml_etree_iterparse      | 97.4 ms                                                                                                               | 97.7 ms: 1.00x slower                                                                                                     |
| scimark_sparse_mat_mult  | 4.86 ms                                                                                                               | 4.87 ms: 1.00x slower                                                                                                     |
| mdp                      | 1.27 sec                                                                                                              | 1.28 sec: 1.00x slower                                                                                                    |
| python_startup_no_site   | 8.83 ms                                                                                                               | 8.86 ms: 1.00x slower                                                                                                     |
| dulwich_log              | 58.5 ms                                                                                                               | 58.8 ms: 1.00x slower                                                                                                     |
| pickle_pure_python       | 333 us                                                                                                                | 335 us: 1.01x slower                                                                                                      |
| unpickle_list            | 5.02 us                                                                                                               | 5.05 us: 1.01x slower                                                                                                     |
| coroutines               | 22.3 ms                                                                                                               | 22.5 ms: 1.01x slower                                                                                                     |
| typing_runtime_protocols | 167 us                                                                                                                | 169 us: 1.01x slower                                                                                                      |
| async_tree_none          | 273 ms                                                                                                                | 276 ms: 1.01x slower                                                                                                      |
| unpickle                 | 14.8 us                                                                                                               | 14.9 us: 1.01x slower                                                                                                     |
| sympy_sum                | 149 ms                                                                                                                | 151 ms: 1.01x slower                                                                                                      |
| 2to3                     | 281 ms                                                                                                                | 285 ms: 1.02x slower                                                                                                      |
| docutils                 | 2.86 sec                                                                                                              | 2.91 sec: 1.02x slower                                                                                                    |
| sympy_expand             | 486 ms                                                                                                                | 494 ms: 1.02x slower                                                                                                      |
| sympy_integrate          | 21.9 ms                                                                                                               | 22.2 ms: 1.02x slower                                                                                                     |
| logging_format           | 6.57 us                                                                                                               | 6.69 us: 1.02x slower                                                                                                     |
| sqlglot_v2_parse         | 1.30 ms                                                                                                               | 1.33 ms: 1.02x slower                                                                                                     |
| sympy_str                | 284 ms                                                                                                                | 289 ms: 1.02x slower                                                                                                      |
| bench_thread_pool        | 974 us                                                                                                                | 993 us: 1.02x slower                                                                                                      |
| meteor_contest           | 120 ms                                                                                                                | 122 ms: 1.02x slower                                                                                                      |
| genshi_xml               | 52.8 ms                                                                                                               | 53.8 ms: 1.02x slower                                                                                                     |
| asyncio_tcp              | 364 ms                                                                                                                | 372 ms: 1.02x slower                                                                                                      |
| chaos                    | 59.0 ms                                                                                                               | 60.2 ms: 1.02x slower                                                                                                     |
| crypto_pyaes             | 76.1 ms                                                                                                               | 77.7 ms: 1.02x slower                                                                                                     |
| deepcopy                 | 276 us                                                                                                                | 282 us: 1.02x slower                                                                                                      |
| sqlglot_v2_transpile     | 1.68 ms                                                                                                               | 1.72 ms: 1.02x slower                                                                                                     |
| many_optionals           | 1.02 ms                                                                                                               | 1.05 ms: 1.02x slower                                                                                                     |
| nqueens                  | 91.1 ms                                                                                                               | 93.6 ms: 1.03x slower                                                                                                     |
| pycparser                | 1.22 sec                                                                                                              | 1.25 sec: 1.03x slower                                                                                                    |
| raytrace                 | 284 ms                                                                                                                | 293 ms: 1.03x slower                                                                                                      |
| sqlglot_v2_normalize     | 112 ms                                                                                                                | 115 ms: 1.03x slower                                                                                                      |
| html5lib                 | 65.5 ms                                                                                                               | 67.6 ms: 1.03x slower                                                                                                     |
| regex_v8                 | 23.3 ms                                                                                                               | 24.1 ms: 1.03x slower                                                                                                     |
| logging_simple           | 5.94 us                                                                                                               | 6.14 us: 1.03x slower                                                                                                     |
| fannkuch                 | 360 ms                                                                                                                | 372 ms: 1.03x slower                                                                                                      |
| sqlglot_v2_optimize      | 55.7 ms                                                                                                               | 58.0 ms: 1.04x slower                                                                                                     |
| gc_traversal             | 6.47 ms                                                                                                               | 6.75 ms: 1.04x slower                                                                                                     |
| scimark_monte_carlo      | 61.8 ms                                                                                                               | 64.5 ms: 1.04x slower                                                                                                     |
| hexiom                   | 5.91 ms                                                                                                               | 6.19 ms: 1.05x slower                                                                                                     |
| async_generators         | 422 ms                                                                                                                | 443 ms: 1.05x slower                                                                                                      |
| nbody                    | 93.0 ms                                                                                                               | 98.2 ms: 1.06x slower                                                                                                     |
| go                       | 119 ms                                                                                                                | 126 ms: 1.06x slower                                                                                                      |
| comprehensions           | 16.4 us                                                                                                               | 17.4 us: 1.06x slower                                                                                                     |
| unpack_sequence          | 45.0 ns                                                                                                               | 51.0 ns: 1.13x slower                                                                                                     |
| Geometric mean           | (ref)                                                                                                                 | 1.01x faster                                                                                                              |

Benchmark hidden because not significant (16): bench_mp_pool, create_gc_cycles, async_tree_io, telco, json_dumps, async_tree_cpu_io_mixed_tg, djangocms, sphinx, asyncio_tcp_ssl, deepcopy_reduce, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, django_template, async_tree_memoization, pylint

- Geometric mean (including insignificant results): 1.009x faster

# HPT report

- Reliability score: 70.04% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.02x