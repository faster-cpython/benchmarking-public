
# Results vs. 3.11.0

- fork: brandtbucher
- ref: shrink_call_more
- machine: linux-x86_64
- commit hash: d02b607
- commit date: 2023-04-04
- overall geometric mean: 1.04x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230404-linux-x86_64-brandtbucher-shrink_call_more-3.12.0a6+-d02b607 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 251 ms: 1.03x faster                                                     |
| chameleon      | 6.47 ms                                                | 6.67 ms: 1.03x slower                                                    |
| docutils       | 2.63 sec                                               | 2.54 sec: 1.03x faster                                                   |
| html5lib       | 64.5 ms                                                | 60.8 ms: 1.06x faster                                                    |
| tornado_http   | 96.3 ms                                                | 90.8 ms: 1.06x faster                                                    |
| Geometric mean | (ref)                                                  | 1.03x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230404-linux-x86_64-brandtbucher-shrink_call_more-3.12.0a6+-d02b607 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| nbody          | 93.1 ms                                                | 88.1 ms: 1.06x faster                                                    |
| pidigits       | 198 ms                                                 | 188 ms: 1.05x faster                                                     |
| float          | 77.2 ms                                                | 74.1 ms: 1.04x faster                                                    |
| Geometric mean | (ref)                                                  | 1.05x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230404-linux-x86_64-brandtbucher-shrink_call_more-3.12.0a6+-d02b607 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.69 ms: 1.08x faster                                                    |
| regex_compile  | 138 ms                                                 | 132 ms: 1.04x faster                                                     |
| regex_v8       | 22.0 ms                                                | 21.7 ms: 1.02x faster                                                    |
| regex_dna      | 204 ms                                                 | 205 ms: 1.01x slower                                                     |
| Geometric mean | (ref)                                                  | 1.03x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230404-linux-x86_64-brandtbucher-shrink_call_more-3.12.0a6+-d02b607 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.49 ms: 1.33x faster                                                    |
| unpickle_pure_python | 228 us                                                 | 199 us: 1.15x faster                                                     |
| json_loads           | 26.5 us                                                | 24.3 us: 1.09x faster                                                    |
| pickle_pure_python   | 306 us                                                 | 284 us: 1.08x faster                                                     |
| xml_etree_parse      | 158 ms                                                 | 148 ms: 1.07x faster                                                     |
| xml_etree_iterparse  | 104 ms                                                 | 99.9 ms: 1.04x faster                                                    |
| pickle_dict          | 31.1 us                                                | 31.4 us: 1.01x slower                                                    |
| pickle               | 10.1 us                                                | 10.5 us: 1.04x slower                                                    |
| xml_etree_process    | 53.9 ms                                                | 56.4 ms: 1.05x slower                                                    |
| unpickle_list        | 4.91 us                                                | 5.17 us: 1.05x slower                                                    |
| pickle_list          | 4.11 us                                                | 4.36 us: 1.06x slower                                                    |
| xml_etree_generate   | 76.2 ms                                                | 82.1 ms: 1.08x slower                                                    |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                             |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230404-linux-x86_64-brandtbucher-shrink_call_more-3.12.0a6+-d02b607 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 8.78 ms: 1.03x slower                                                    |
| python_startup_no_site | 6.01 ms                                                | 6.49 ms: 1.08x slower                                                    |
| Geometric mean         | (ref)                                                  | 1.05x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230404-linux-x86_64-brandtbucher-shrink_call_more-3.12.0a6+-d02b607 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_xml      | 51.8 ms                                                | 48.0 ms: 1.08x faster                                                    |
| genshi_text     | 21.6 ms                                                | 21.2 ms: 1.02x faster                                                    |
| mako            | 10.1 ms                                                | 10.2 ms: 1.01x slower                                                    |
| django_template | 32.6 ms                                                | 33.8 ms: 1.04x slower                                                    |
| Geometric mean  | (ref)                                                  | 1.01x faster                                                             |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230404-linux-x86_64-brandtbucher-shrink_call_more-3.12.0a6+-d02b607 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| generators              | 73.5 ms                                                | 29.3 ms: 2.51x faster                                                    |
| asyncio_tcp             | 922 ms                                                 | 500 ms: 1.84x faster                                                     |
| json_dumps              | 12.6 ms                                                | 9.49 ms: 1.33x faster                                                    |
| mypy2                   | 420 ms                                                 | 331 ms: 1.27x faster                                                     |
| unpickle_pure_python    | 228 us                                                 | 199 us: 1.15x faster                                                     |
| deltablue               | 3.67 ms                                                | 3.25 ms: 1.13x faster                                                    |
| aiohttp                 | 1.10 ms                                                | 1.01 ms: 1.09x faster                                                    |
| gunicorn                | 1.18 ms                                                | 1.08 ms: 1.09x faster                                                    |
| json_loads              | 26.5 us                                                | 24.3 us: 1.09x faster                                                    |
| scimark_sparse_mat_mult | 4.50 ms                                                | 4.13 ms: 1.09x faster                                                    |
| coroutines              | 25.5 ms                                                | 23.5 ms: 1.09x faster                                                    |
| regex_effbot            | 3.99 ms                                                | 3.69 ms: 1.08x faster                                                    |
| pycparser               | 1.18 sec                                               | 1.09 sec: 1.08x faster                                                   |
| genshi_xml              | 51.8 ms                                                | 48.0 ms: 1.08x faster                                                    |
| deepcopy_memo           | 37.0 us                                                | 34.4 us: 1.08x faster                                                    |
| pickle_pure_python      | 306 us                                                 | 284 us: 1.08x faster                                                     |
| xml_etree_parse         | 158 ms                                                 | 148 ms: 1.07x faster                                                     |
| json                    | 4.94 ms                                                | 4.61 ms: 1.07x faster                                                    |
| raytrace                | 297 ms                                                 | 279 ms: 1.06x faster                                                     |
| scimark_fft             | 328 ms                                                 | 309 ms: 1.06x faster                                                     |
| html5lib                | 64.5 ms                                                | 60.8 ms: 1.06x faster                                                    |
| tornado_http            | 96.3 ms                                                | 90.8 ms: 1.06x faster                                                    |
| spectral_norm           | 100 ms                                                 | 94.5 ms: 1.06x faster                                                    |
| nbody                   | 93.1 ms                                                | 88.1 ms: 1.06x faster                                                    |
| logging_format          | 6.68 us                                                | 6.34 us: 1.05x faster                                                    |
| pidigits                | 198 ms                                                 | 188 ms: 1.05x faster                                                     |
| chaos                   | 69.2 ms                                                | 65.8 ms: 1.05x faster                                                    |
| richards                | 45.7 ms                                                | 43.5 ms: 1.05x faster                                                    |
| logging_simple          | 6.03 us                                                | 5.76 us: 1.05x faster                                                    |
| regex_compile           | 138 ms                                                 | 132 ms: 1.04x faster                                                     |
| float                   | 77.2 ms                                                | 74.1 ms: 1.04x faster                                                    |
| coverage                | 100 ms                                                 | 96.1 ms: 1.04x faster                                                    |
| xml_etree_iterparse     | 104 ms                                                 | 99.9 ms: 1.04x faster                                                    |
| bench_thread_pool       | 819 us                                                 | 790 us: 1.04x faster                                                     |
| docutils                | 2.63 sec                                               | 2.54 sec: 1.03x faster                                                   |
| hexiom                  | 6.37 ms                                                | 6.16 ms: 1.03x faster                                                    |
| 2to3                    | 259 ms                                                 | 251 ms: 1.03x faster                                                     |
| sqlglot_optimize        | 53.1 ms                                                | 51.6 ms: 1.03x faster                                                    |
| logging_silent          | 101 ns                                                 | 98.3 ns: 1.03x faster                                                    |
| deepcopy                | 342 us                                                 | 333 us: 1.03x faster                                                     |
| sympy_integrate         | 21.0 ms                                                | 20.5 ms: 1.03x faster                                                    |
| mdp                     | 2.62 sec                                               | 2.55 sec: 1.02x faster                                                   |
| sympy_expand            | 475 ms                                                 | 464 ms: 1.02x faster                                                     |
| meteor_contest          | 107 ms                                                 | 104 ms: 1.02x faster                                                     |
| sqlglot_normalize       | 108 ms                                                 | 105 ms: 1.02x faster                                                     |
| go                      | 140 ms                                                 | 137 ms: 1.02x faster                                                     |
| sympy_str               | 290 ms                                                 | 284 ms: 1.02x faster                                                     |
| sqlalchemy_declarative  | 138 ms                                                 | 136 ms: 1.02x faster                                                     |
| pprint_pformat          | 1.46 sec                                               | 1.43 sec: 1.02x faster                                                   |
| scimark_lu              | 110 ms                                                 | 108 ms: 1.02x faster                                                     |
| unpack_sequence         | 43.1 ns                                                | 42.4 ns: 1.02x faster                                                    |
| genshi_text             | 21.6 ms                                                | 21.2 ms: 1.02x faster                                                    |
| scimark_sor             | 118 ms                                                 | 116 ms: 1.02x faster                                                     |
| regex_v8                | 22.0 ms                                                | 21.7 ms: 1.02x faster                                                    |
| pathlib                 | 18.2 ms                                                | 18.0 ms: 1.01x faster                                                    |
| async_tree_none         | 526 ms                                                 | 521 ms: 1.01x faster                                                     |
| pprint_safe_repr        | 701 ms                                                 | 695 ms: 1.01x faster                                                     |
| nqueens                 | 83.4 ms                                                | 82.7 ms: 1.01x faster                                                    |
| create_gc_cycles        | 1.49 ms                                                | 1.48 ms: 1.01x faster                                                    |
| regex_dna               | 204 ms                                                 | 205 ms: 1.01x slower                                                     |
| mako                    | 10.1 ms                                                | 10.2 ms: 1.01x slower                                                    |
| scimark_monte_carlo     | 68.1 ms                                                | 68.6 ms: 1.01x slower                                                    |
| crypto_pyaes            | 74.7 ms                                                | 75.3 ms: 1.01x slower                                                    |
| pickle_dict             | 31.1 us                                                | 31.4 us: 1.01x slower                                                    |
| deepcopy_reduce         | 2.94 us                                                | 2.99 us: 1.02x slower                                                    |
| sqlglot_transpile       | 1.70 ms                                                | 1.75 ms: 1.03x slower                                                    |
| python_startup          | 8.52 ms                                                | 8.78 ms: 1.03x slower                                                    |
| chameleon               | 6.47 ms                                                | 6.67 ms: 1.03x slower                                                    |
| thrift                  | 756 us                                                 | 783 us: 1.04x slower                                                     |
| django_template         | 32.6 ms                                                | 33.8 ms: 1.04x slower                                                    |
| sqlglot_parse           | 1.40 ms                                                | 1.45 ms: 1.04x slower                                                    |
| pickle                  | 10.1 us                                                | 10.5 us: 1.04x slower                                                    |
| xml_etree_process       | 53.9 ms                                                | 56.4 ms: 1.05x slower                                                    |
| unpickle_list           | 4.91 us                                                | 5.17 us: 1.05x slower                                                    |
| sqlite_synth            | 2.52 us                                                | 2.66 us: 1.05x slower                                                    |
| pyflate                 | 418 ms                                                 | 441 ms: 1.05x slower                                                     |
| pickle_list             | 4.11 us                                                | 4.36 us: 1.06x slower                                                    |
| comprehensions          | 22.4 us                                                | 23.8 us: 1.06x slower                                                    |
| gc_traversal            | 4.02 ms                                                | 4.32 ms: 1.07x slower                                                    |
| xml_etree_generate      | 76.2 ms                                                | 82.1 ms: 1.08x slower                                                    |
| python_startup_no_site  | 6.01 ms                                                | 6.49 ms: 1.08x slower                                                    |
| async_generators        | 368 ms                                                 | 417 ms: 1.13x slower                                                     |
| dask                    | 360 ms                                                 | 510 ms: 1.42x slower                                                     |
| Geometric mean          | (ref)                                                  | 1.04x faster                                                             |

Benchmark hidden because not significant (11): unpickle, djangocms, sqlalchemy_imperative, async_tree_cpu_io_mixed, async_tree_io, telco, sympy_sum, bench_mp_pool, fannkuch, dulwich_log, async_tree_memoization
Ignored benchmarks (6) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp_ssl, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x
