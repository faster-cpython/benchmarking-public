
# Results vs. 3.11.0

- fork: ericsnowcurrently
- ref: tstate_current_as_th
- machine: darwin-arm64
- commit hash: 2332a2e
- commit date: 2023-04-07
- overall geometric mean: 1.04x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230407-darwin-arm64-ericsnowcurrently-tstate_current_as_th-3.12.0a7+-2332a2e |
|----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 161 ms                                                              | 173 ms: 1.08x slower                                                              |
| chameleon      | 4.55 ms                                                             | 4.69 ms: 1.03x slower                                                             |
| docutils       | 1.47 sec                                                            | 1.54 sec: 1.05x slower                                                            |
| html5lib       | 34.8 ms                                                             | 37.7 ms: 1.08x slower                                                             |
| Geometric mean | (ref)                                                               | 1.05x slower                                                                      |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230407-darwin-arm64-ericsnowcurrently-tstate_current_as_th-3.12.0a7+-2332a2e |
|----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| pidigits       | 281 ms                                                              | 280 ms: 1.00x faster                                                              |
| nbody          | 65.5 ms                                                             | 65.6 ms: 1.00x slower                                                             |
| float          | 53.0 ms                                                             | 56.2 ms: 1.06x slower                                                             |
| Geometric mean | (ref)                                                               | 1.02x slower                                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230407-darwin-arm64-ericsnowcurrently-tstate_current_as_th-3.12.0a7+-2332a2e |
|----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_dna      | 151 ms                                                              | 152 ms: 1.00x slower                                                              |
| regex_effbot   | 2.63 ms                                                             | 2.65 ms: 1.01x slower                                                             |
| regex_v8       | 16.1 ms                                                             | 16.2 ms: 1.01x slower                                                             |
| regex_compile  | 76.6 ms                                                             | 78.5 ms: 1.02x slower                                                             |
| Geometric mean | (ref)                                                               | 1.01x slower                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230407-darwin-arm64-ericsnowcurrently-tstate_current_as_th-3.12.0a7+-2332a2e |
|----------------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| json_dumps           | 7.59 ms                                                             | 6.39 ms: 1.19x faster                                                             |
| unpickle_pure_python | 158 us                                                              | 148 us: 1.07x faster                                                              |
| unpickle             | 9.66 us                                                             | 9.27 us: 1.04x faster                                                             |
| pickle_pure_python   | 198 us                                                              | 192 us: 1.03x faster                                                              |
| xml_etree_parse      | 106 ms                                                              | 105 ms: 1.01x faster                                                              |
| json_loads           | 16.0 us                                                             | 16.4 us: 1.02x slower                                                             |
| pickle_dict          | 17.9 us                                                             | 18.7 us: 1.05x slower                                                             |
| xml_etree_iterparse  | 69.2 ms                                                             | 73.4 ms: 1.06x slower                                                             |
| pickle               | 7.17 us                                                             | 7.65 us: 1.07x slower                                                             |
| xml_etree_process    | 35.0 ms                                                             | 38.5 ms: 1.10x slower                                                             |
| unpickle_list        | 2.63 us                                                             | 2.90 us: 1.10x slower                                                             |
| pickle_list          | 2.83 us                                                             | 3.12 us: 1.10x slower                                                             |
| xml_etree_generate   | 48.2 ms                                                             | 56.2 ms: 1.17x slower                                                             |
| Geometric mean       | (ref)                                                               | 1.02x slower                                                                      |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230407-darwin-arm64-ericsnowcurrently-tstate_current_as_th-3.12.0a7+-2332a2e |
|------------------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup         | 12.3 ms                                                             | 11.9 ms: 1.04x faster                                                             |
| python_startup_no_site | 10.1 ms                                                             | 9.92 ms: 1.01x faster                                                             |
| Geometric mean         | (ref)                                                               | 1.03x faster                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230407-darwin-arm64-ericsnowcurrently-tstate_current_as_th-3.12.0a7+-2332a2e |
|-----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| mako            | 8.42 ms                                                             | 7.34 ms: 1.15x faster                                                             |
| genshi_text     | 15.3 ms                                                             | 14.7 ms: 1.04x faster                                                             |
| genshi_xml      | 29.9 ms                                                             | 30.3 ms: 1.01x slower                                                             |
| django_template | 21.1 ms                                                             | 22.6 ms: 1.07x slower                                                             |
| Geometric mean  | (ref)                                                               | 1.02x faster                                                                      |

All benchmarks:
===============

| Benchmark               | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230407-darwin-arm64-ericsnowcurrently-tstate_current_as_th-3.12.0a7+-2332a2e |
|-------------------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| asyncio_tcp             | 651 ms                                                              | 448 ms: 1.45x faster                                                              |
| json_dumps              | 7.59 ms                                                             | 6.39 ms: 1.19x faster                                                             |
| mako                    | 8.42 ms                                                             | 7.34 ms: 1.15x faster                                                             |
| generators              | 28.6 ms                                                             | 26.2 ms: 1.09x faster                                                             |
| scimark_sparse_mat_mult | 3.19 ms                                                             | 2.95 ms: 1.08x faster                                                             |
| deltablue               | 2.81 ms                                                             | 2.62 ms: 1.07x faster                                                             |
| unpickle_pure_python    | 158 us                                                              | 148 us: 1.07x faster                                                              |
| hexiom                  | 4.73 ms                                                             | 4.47 ms: 1.06x faster                                                             |
| sqlglot_parse           | 956 us                                                              | 905 us: 1.06x faster                                                              |
| richards                | 32.2 ms                                                             | 30.8 ms: 1.04x faster                                                             |
| unpickle                | 9.66 us                                                             | 9.27 us: 1.04x faster                                                             |
| genshi_text             | 15.3 ms                                                             | 14.7 ms: 1.04x faster                                                             |
| sqlglot_transpile       | 1.12 ms                                                             | 1.08 ms: 1.04x faster                                                             |
| python_startup          | 12.3 ms                                                             | 11.9 ms: 1.04x faster                                                             |
| pickle_pure_python      | 198 us                                                              | 192 us: 1.03x faster                                                              |
| scimark_fft             | 200 ms                                                              | 194 ms: 1.03x faster                                                              |
| create_gc_cycles        | 722 us                                                              | 707 us: 1.02x faster                                                              |
| deepcopy_memo           | 26.3 us                                                             | 25.8 us: 1.02x faster                                                             |
| python_startup_no_site  | 10.1 ms                                                             | 9.92 ms: 1.01x faster                                                             |
| xml_etree_parse         | 106 ms                                                              | 105 ms: 1.01x faster                                                              |
| logging_silent          | 68.0 ns                                                             | 67.8 ns: 1.00x faster                                                             |
| pidigits                | 281 ms                                                              | 280 ms: 1.00x faster                                                              |
| chaos                   | 49.4 ms                                                             | 49.3 ms: 1.00x faster                                                             |
| nbody                   | 65.5 ms                                                             | 65.6 ms: 1.00x slower                                                             |
| regex_dna               | 151 ms                                                              | 152 ms: 1.00x slower                                                              |
| unpack_sequence         | 33.5 ns                                                             | 33.8 ns: 1.01x slower                                                             |
| coverage                | 58.4 ms                                                             | 58.8 ms: 1.01x slower                                                             |
| regex_effbot            | 2.63 ms                                                             | 2.65 ms: 1.01x slower                                                             |
| regex_v8                | 16.1 ms                                                             | 16.2 ms: 1.01x slower                                                             |
| meteor_contest          | 73.3 ms                                                             | 74.0 ms: 1.01x slower                                                             |
| spectral_norm           | 72.5 ms                                                             | 73.3 ms: 1.01x slower                                                             |
| genshi_xml              | 29.9 ms                                                             | 30.3 ms: 1.01x slower                                                             |
| mdp                     | 1.54 sec                                                            | 1.56 sec: 1.01x slower                                                            |
| scimark_lu              | 72.2 ms                                                             | 73.3 ms: 1.02x slower                                                             |
| json                    | 2.77 ms                                                             | 2.83 ms: 1.02x slower                                                             |
| regex_compile           | 76.6 ms                                                             | 78.5 ms: 1.02x slower                                                             |
| json_loads              | 16.0 us                                                             | 16.4 us: 1.02x slower                                                             |
| async_tree_cpu_io_mixed | 534 ms                                                              | 548 ms: 1.03x slower                                                              |
| sqlalchemy_imperative   | 7.26 ms                                                             | 7.48 ms: 1.03x slower                                                             |
| chameleon               | 4.55 ms                                                             | 4.69 ms: 1.03x slower                                                             |
| deepcopy                | 224 us                                                              | 231 us: 1.03x slower                                                              |
| async_tree_none         | 285 ms                                                              | 295 ms: 1.04x slower                                                              |
| dulwich_log             | 29.7 ms                                                             | 30.9 ms: 1.04x slower                                                             |
| comprehensions          | 16.1 us                                                             | 16.8 us: 1.05x slower                                                             |
| pickle_dict             | 17.9 us                                                             | 18.7 us: 1.05x slower                                                             |
| bench_thread_pool       | 474 us                                                              | 497 us: 1.05x slower                                                              |
| docutils                | 1.47 sec                                                            | 1.54 sec: 1.05x slower                                                            |
| nqueens                 | 62.4 ms                                                             | 65.7 ms: 1.05x slower                                                             |
| crypto_pyaes            | 51.8 ms                                                             | 54.7 ms: 1.06x slower                                                             |
| go                      | 109 ms                                                              | 115 ms: 1.06x slower                                                              |
| sympy_integrate         | 11.5 ms                                                             | 12.2 ms: 1.06x slower                                                             |
| float                   | 53.0 ms                                                             | 56.2 ms: 1.06x slower                                                             |
| xml_etree_iterparse     | 69.2 ms                                                             | 73.4 ms: 1.06x slower                                                             |
| async_tree_io           | 707 ms                                                              | 752 ms: 1.06x slower                                                              |
| pprint_pformat          | 946 ms                                                              | 1.01 sec: 1.07x slower                                                            |
| pickle                  | 7.17 us                                                             | 7.65 us: 1.07x slower                                                             |
| bench_mp_pool           | 43.8 ms                                                             | 46.8 ms: 1.07x slower                                                             |
| gc_traversal            | 2.41 ms                                                             | 2.59 ms: 1.07x slower                                                             |
| django_template         | 21.1 ms                                                             | 22.6 ms: 1.07x slower                                                             |
| pprint_safe_repr        | 463 ms                                                              | 497 ms: 1.07x slower                                                              |
| 2to3                    | 161 ms                                                              | 173 ms: 1.08x slower                                                              |
| deepcopy_reduce         | 1.91 us                                                             | 2.05 us: 1.08x slower                                                             |
| coroutines              | 17.7 ms                                                             | 19.1 ms: 1.08x slower                                                             |
| sqlalchemy_declarative  | 62.6 ms                                                             | 67.5 ms: 1.08x slower                                                             |
| sqlglot_optimize        | 31.2 ms                                                             | 33.7 ms: 1.08x slower                                                             |
| sqlglot_normalize       | 171 ms                                                              | 185 ms: 1.08x slower                                                              |
| html5lib                | 34.8 ms                                                             | 37.7 ms: 1.08x slower                                                             |
| telco                   | 3.40 ms                                                             | 3.68 ms: 1.08x slower                                                             |
| logging_simple          | 3.49 us                                                             | 3.79 us: 1.09x slower                                                             |
| scimark_sor             | 82.9 ms                                                             | 90.0 ms: 1.09x slower                                                             |
| sympy_sum               | 86.0 ms                                                             | 93.6 ms: 1.09x slower                                                             |
| logging_format          | 3.77 us                                                             | 4.11 us: 1.09x slower                                                             |
| fannkuch                | 260 ms                                                              | 284 ms: 1.09x slower                                                              |
| sympy_str               | 151 ms                                                              | 166 ms: 1.09x slower                                                              |
| sympy_expand            | 243 ms                                                              | 267 ms: 1.10x slower                                                              |
| xml_etree_process       | 35.0 ms                                                             | 38.5 ms: 1.10x slower                                                             |
| pyflate                 | 309 ms                                                              | 341 ms: 1.10x slower                                                              |
| unpickle_list           | 2.63 us                                                             | 2.90 us: 1.10x slower                                                             |
| pickle_list             | 2.83 us                                                             | 3.12 us: 1.10x slower                                                             |
| scimark_monte_carlo     | 46.5 ms                                                             | 52.2 ms: 1.12x slower                                                             |
| thrift                  | 431 us                                                              | 501 us: 1.16x slower                                                              |
| raytrace                | 207 ms                                                              | 240 ms: 1.16x slower                                                              |
| xml_etree_generate      | 48.2 ms                                                             | 56.2 ms: 1.17x slower                                                             |
| sqlite_synth            | 1.28 us                                                             | 1.54 us: 1.20x slower                                                             |
| dask                    | 226 ms                                                              | 330 ms: 1.46x slower                                                              |
| async_generators        | 195 ms                                                              | 301 ms: 1.54x slower                                                              |
| Geometric mean          | (ref)                                                               | 1.04x slower                                                                      |

Benchmark hidden because not significant (5): tornado_http, pathlib, pycparser, async_tree_memoization, mypy2
Ignored benchmarks (4) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509.json: aiohttp, flaskblogging, gunicorn, pylint
