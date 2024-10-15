# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: reset_counters
- machine: linux-x86_64
- commit hash: ebcfcaf
- commit date: 2024-10-14
- overall geometric mean: 1.03x faster
- HPT reliability: 99.75%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241014-linux-x86_64-brandtbucher-reset_counters-3.14.0a0-ebcfcaf |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 278 ms: 1.01x slower                                                  |
| docutils       | 2.83 sec                                                   | 2.87 sec: 1.01x slower                                                |
| html5lib       | 67.2 ms                                                    | 62.7 ms: 1.07x faster                                                 |
| tornado_http   | 94.6 ms                                                    | 93.7 ms: 1.01x faster                                                 |
| Geometric mean | (ref)                                                      | 1.01x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241014-linux-x86_64-brandtbucher-reset_counters-3.14.0a0-ebcfcaf |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 78.9 ms                                                    | 72.4 ms: 1.09x faster                                                 |
| nbody          | 88.3 ms                                                    | 83.5 ms: 1.06x faster                                                 |
| pidigits       | 191 ms                                                     | 185 ms: 1.03x faster                                                  |
| Geometric mean | (ref)                                                      | 1.06x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241014-linux-x86_64-brandtbucher-reset_counters-3.14.0a0-ebcfcaf |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_dna      | 221 ms                                                     | 209 ms: 1.06x faster                                                  |
| regex_v8       | 25.1 ms                                                    | 24.1 ms: 1.04x faster                                                 |
| regex_effbot   | 3.67 ms                                                    | 3.61 ms: 1.02x faster                                                 |
| regex_compile  | 137 ms                                                     | 139 ms: 1.02x slower                                                  |
| Geometric mean | (ref)                                                      | 1.03x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241014-linux-x86_64-brandtbucher-reset_counters-3.14.0a0-ebcfcaf |
|----------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_generate   | 87.4 ms                                                    | 78.4 ms: 1.12x faster                                                 |
| xml_etree_process    | 61.2 ms                                                    | 54.9 ms: 1.11x faster                                                 |
| xml_etree_parse      | 162 ms                                                     | 146 ms: 1.11x faster                                                  |
| tomli_loads          | 2.12 sec                                                   | 1.91 sec: 1.11x faster                                                |
| xml_etree_iterparse  | 107 ms                                                     | 98.0 ms: 1.10x faster                                                 |
| json_loads           | 28.9 us                                                    | 26.6 us: 1.09x faster                                                 |
| unpickle_pure_python | 218 us                                                     | 215 us: 1.02x faster                                                  |
| pickle_dict          | 34.8 us                                                    | 35.2 us: 1.01x slower                                                 |
| pickle_list          | 5.11 us                                                    | 5.17 us: 1.01x slower                                                 |
| unpickle_list        | 5.34 us                                                    | 5.41 us: 1.01x slower                                                 |
| pickle_pure_python   | 305 us                                                     | 310 us: 1.01x slower                                                  |
| pickle               | 11.5 us                                                    | 11.8 us: 1.02x slower                                                 |
| json_dumps           | 10.7 ms                                                    | 11.2 ms: 1.04x slower                                                 |
| Geometric mean       | (ref)                                                      | 1.04x faster                                                          |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241014-linux-x86_64-brandtbucher-reset_counters-3.14.0a0-ebcfcaf |
|------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                                 |
| python_startup_no_site | 7.11 ms                                                    | 7.07 ms: 1.00x faster                                                 |
| Geometric mean         | (ref)                                                      | 1.01x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241014-linux-x86_64-brandtbucher-reset_counters-3.14.0a0-ebcfcaf |
|-----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 10.0 ms: 1.12x faster                                                 |
| django_template | 34.8 ms                                                    | 36.0 ms: 1.04x slower                                                 |
| genshi_text     | 23.7 ms                                                    | 25.1 ms: 1.06x slower                                                 |
| genshi_xml      | 51.6 ms                                                    | 58.0 ms: 1.12x slower                                                 |
| Geometric mean  | (ref)                                                      | 1.03x slower                                                          |

All benchmarks:
===============

| Benchmark               | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241014-linux-x86_64-brandtbucher-reset_counters-3.14.0a0-ebcfcaf |
|-------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy_memo           | 39.7 us                                                    | 27.4 us: 1.45x faster                                                 |
| deepcopy                | 367 us                                                     | 264 us: 1.39x faster                                                  |
| richards_super          | 57.4 ms                                                    | 45.2 ms: 1.27x faster                                                 |
| deepcopy_reduce         | 3.35 us                                                    | 2.66 us: 1.26x faster                                                 |
| scimark_fft             | 392 ms                                                     | 312 ms: 1.26x faster                                                  |
| richards                | 50.9 ms                                                    | 40.7 ms: 1.25x faster                                                 |
| crypto_pyaes            | 77.5 ms                                                    | 66.7 ms: 1.16x faster                                                 |
| spectral_norm           | 116 ms                                                     | 101 ms: 1.14x faster                                                  |
| bpe_tokeniser           | 5.02 sec                                                   | 4.39 sec: 1.14x faster                                                |
| scimark_sparse_mat_mult | 5.27 ms                                                    | 4.62 ms: 1.14x faster                                                 |
| mako                    | 11.2 ms                                                    | 10.0 ms: 1.12x faster                                                 |
| xml_etree_generate      | 87.4 ms                                                    | 78.4 ms: 1.12x faster                                                 |
| coverage                | 93.1 ms                                                    | 83.5 ms: 1.11x faster                                                 |
| xml_etree_process       | 61.2 ms                                                    | 54.9 ms: 1.11x faster                                                 |
| xml_etree_parse         | 162 ms                                                     | 146 ms: 1.11x faster                                                  |
| tomli_loads             | 2.12 sec                                                   | 1.91 sec: 1.11x faster                                                |
| telco                   | 8.41 ms                                                    | 7.62 ms: 1.10x faster                                                 |
| scimark_lu              | 122 ms                                                     | 110 ms: 1.10x faster                                                  |
| xml_etree_iterparse     | 107 ms                                                     | 98.0 ms: 1.10x faster                                                 |
| go                      | 145 ms                                                     | 132 ms: 1.09x faster                                                  |
| mdp                     | 2.79 sec                                                   | 2.55 sec: 1.09x faster                                                |
| float                   | 78.9 ms                                                    | 72.4 ms: 1.09x faster                                                 |
| scimark_monte_carlo     | 69.2 ms                                                    | 63.5 ms: 1.09x faster                                                 |
| pathlib                 | 17.3 ms                                                    | 15.9 ms: 1.09x faster                                                 |
| scimark_sor             | 127 ms                                                     | 117 ms: 1.09x faster                                                  |
| json_loads              | 28.9 us                                                    | 26.6 us: 1.09x faster                                                 |
| pyflate                 | 484 ms                                                     | 447 ms: 1.08x faster                                                  |
| json                    | 5.31 ms                                                    | 4.93 ms: 1.08x faster                                                 |
| html5lib                | 67.2 ms                                                    | 62.7 ms: 1.07x faster                                                 |
| logging_format          | 6.47 us                                                    | 6.04 us: 1.07x faster                                                 |
| regex_dna               | 221 ms                                                     | 209 ms: 1.06x faster                                                  |
| sqlite_synth            | 2.99 us                                                    | 2.82 us: 1.06x faster                                                 |
| nbody                   | 88.3 ms                                                    | 83.5 ms: 1.06x faster                                                 |
| fannkuch                | 402 ms                                                     | 381 ms: 1.06x faster                                                  |
| logging_silent          | 105 ns                                                     | 99.8 ns: 1.05x faster                                                 |
| thrift                  | 823 us                                                     | 785 us: 1.05x faster                                                  |
| logging_simple          | 5.74 us                                                    | 5.48 us: 1.05x faster                                                 |
| pprint_pformat          | 1.56 sec                                                   | 1.49 sec: 1.05x faster                                                |
| pprint_safe_repr        | 758 ms                                                     | 728 ms: 1.04x faster                                                  |
| regex_v8                | 25.1 ms                                                    | 24.1 ms: 1.04x faster                                                 |
| chaos                   | 61.3 ms                                                    | 59.1 ms: 1.04x faster                                                 |
| pidigits                | 191 ms                                                     | 185 ms: 1.03x faster                                                  |
| meteor_contest          | 110 ms                                                     | 107 ms: 1.02x faster                                                  |
| asyncio_tcp             | 508 ms                                                     | 496 ms: 1.02x faster                                                  |
| asyncio_tcp_ssl         | 1.84 sec                                                   | 1.80 sec: 1.02x faster                                                |
| asyncio_websockets      | 567 ms                                                     | 554 ms: 1.02x faster                                                  |
| python_startup          | 10.8 ms                                                    | 10.5 ms: 1.02x faster                                                 |
| create_gc_cycles        | 1.82 ms                                                    | 1.78 ms: 1.02x faster                                                 |
| regex_effbot            | 3.67 ms                                                    | 3.61 ms: 1.02x faster                                                 |
| unpickle_pure_python    | 218 us                                                     | 215 us: 1.02x faster                                                  |
| deltablue               | 3.25 ms                                                    | 3.22 ms: 1.01x faster                                                 |
| tornado_http            | 94.6 ms                                                    | 93.7 ms: 1.01x faster                                                 |
| python_startup_no_site  | 7.11 ms                                                    | 7.07 ms: 1.00x faster                                                 |
| dulwich_log             | 67.2 ms                                                    | 67.5 ms: 1.01x slower                                                 |
| gc_traversal            | 3.98 ms                                                    | 4.01 ms: 1.01x slower                                                 |
| pickle_dict             | 34.8 us                                                    | 35.2 us: 1.01x slower                                                 |
| pickle_list             | 5.11 us                                                    | 5.17 us: 1.01x slower                                                 |
| unpickle_list           | 5.34 us                                                    | 5.41 us: 1.01x slower                                                 |
| pickle_pure_python      | 305 us                                                     | 310 us: 1.01x slower                                                  |
| 2to3                    | 274 ms                                                     | 278 ms: 1.01x slower                                                  |
| docutils                | 2.83 sec                                                   | 2.87 sec: 1.01x slower                                                |
| comprehensions          | 16.6 us                                                    | 16.9 us: 1.01x slower                                                 |
| regex_compile           | 137 ms                                                     | 139 ms: 1.02x slower                                                  |
| sqlglot_transpile       | 1.63 ms                                                    | 1.67 ms: 1.02x slower                                                 |
| pickle                  | 11.5 us                                                    | 11.8 us: 1.02x slower                                                 |
| async_generators        | 442 ms                                                     | 454 ms: 1.03x slower                                                  |
| sqlglot_normalize       | 110 ms                                                     | 114 ms: 1.03x slower                                                  |
| django_template         | 34.8 ms                                                    | 36.0 ms: 1.04x slower                                                 |
| json_dumps              | 10.7 ms                                                    | 11.2 ms: 1.04x slower                                                 |
| bench_thread_pool       | 834 us                                                     | 871 us: 1.04x slower                                                  |
| sympy_expand            | 473 ms                                                     | 498 ms: 1.05x slower                                                  |
| raytrace                | 267 ms                                                     | 282 ms: 1.06x slower                                                  |
| sympy_str               | 282 ms                                                     | 300 ms: 1.06x slower                                                  |
| genshi_text             | 23.7 ms                                                    | 25.1 ms: 1.06x slower                                                 |
| nqueens                 | 81.4 ms                                                    | 86.5 ms: 1.06x slower                                                 |
| sqlglot_optimize        | 55.5 ms                                                    | 59.3 ms: 1.07x slower                                                 |
| hexiom                  | 6.30 ms                                                    | 7.00 ms: 1.11x slower                                                 |
| sympy_sum               | 156 ms                                                     | 175 ms: 1.12x slower                                                  |
| genshi_xml              | 51.6 ms                                                    | 58.0 ms: 1.12x slower                                                 |
| sympy_integrate         | 20.5 ms                                                    | 23.2 ms: 1.13x slower                                                 |
| pylint                  | 317 ms                                                     | 373 ms: 1.18x slower                                                  |
| generators              | 29.6 ms                                                    | 35.3 ms: 1.19x slower                                                 |
| bench_mp_pool           | 23.9 ms                                                    | 60.8 ms: 2.54x slower                                                 |
| Geometric mean          | (ref)                                                      | 1.03x faster                                                          |

Benchmark hidden because not significant (5): unpickle, pycparser, typing_runtime_protocols, sqlglot_parse, coroutines
Ignored benchmarks (15) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_io, async_tree_io_tg, async_tree_memoization, async_tree_memoization_tg, async_tree_none, async_tree_none_tg, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20241014-3.14.0a0-ebcfcaf-JIT/bm-20241014-linux-x86_64-brandtbucher-reset_counters-3.14.0a0-ebcfcaf.json: unpack_sequence

# HPT report

- Reliability score: 99.75% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.07x