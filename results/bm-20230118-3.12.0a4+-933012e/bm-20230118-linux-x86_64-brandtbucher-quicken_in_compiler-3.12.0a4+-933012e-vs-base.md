
# Results vs. base

- fork: brandtbucher
- ref: quicken_in_compiler
- machine: linux-x86_64
- commit hash: 933012e
- commit date: 2023-01-18
- overall geometric mean: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230201-linux-x86_64-python-95fb0e02582b5673eff4-3.12.0a4+-95fb0e0 | bm-20230118-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-933012e |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 251 ms                                                                 | 249 ms: 1.01x faster                                                        |
| chameleon      | 6.41 ms                                                                | 6.37 ms: 1.01x faster                                                       |
| tornado_http   | 93.7 ms                                                                | 94.3 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                                |

Benchmark hidden because not significant (2): docutils, html5lib

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230201-linux-x86_64-python-95fb0e02582b5673eff4-3.12.0a4+-95fb0e0 | bm-20230118-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-933012e |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 96.0 ms                                                                | 94.1 ms: 1.02x faster                                                       |
| pidigits       | 193 ms                                                                 | 189 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                                |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230201-linux-x86_64-python-95fb0e02582b5673eff4-3.12.0a4+-95fb0e0 | bm-20230118-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-933012e |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 201 ms                                                                 | 207 ms: 1.03x slower                                                        |
| regex_effbot   | 3.36 ms                                                                | 3.51 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                                  | 1.02x slower                                                                |

Benchmark hidden because not significant (2): regex_compile, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230201-linux-x86_64-python-95fb0e02582b5673eff4-3.12.0a4+-95fb0e0 | bm-20230118-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-933012e |
|----------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 200 us                                                                 | 196 us: 1.02x faster                                                        |
| json_dumps           | 9.52 ms                                                                | 9.32 ms: 1.02x faster                                                       |
| pickle_pure_python   | 285 us                                                                 | 280 us: 1.02x faster                                                        |
| json_loads           | 24.2 us                                                                | 24.1 us: 1.01x faster                                                       |
| xml_etree_parse      | 147 ms                                                                 | 148 ms: 1.01x slower                                                        |
| pickle               | 10.1 us                                                                | 10.2 us: 1.01x slower                                                       |
| xml_etree_iterparse  | 101 ms                                                                 | 102 ms: 1.01x slower                                                        |
| xml_etree_process    | 53.4 ms                                                                | 54.1 ms: 1.01x slower                                                       |
| unpickle_list        | 5.01 us                                                                | 5.09 us: 1.02x slower                                                       |
| xml_etree_generate   | 77.1 ms                                                                | 78.5 ms: 1.02x slower                                                       |
| pickle_dict          | 31.0 us                                                                | 31.6 us: 1.02x slower                                                       |
| unpickle             | 13.3 us                                                                | 14.0 us: 1.05x slower                                                       |
| Geometric mean       | (ref)                                                                  | 1.01x slower                                                                |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230201-linux-x86_64-python-95fb0e02582b5673eff4-3.12.0a4+-95fb0e0 | bm-20230118-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-933012e |
|------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 6.48 ms                                                                | 6.39 ms: 1.01x faster                                                       |
| python_startup         | 8.95 ms                                                                | 8.85 ms: 1.01x faster                                                       |
| Geometric mean         | (ref)                                                                  | 1.01x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20230201-linux-x86_64-python-95fb0e02582b5673eff4-3.12.0a4+-95fb0e0 | bm-20230118-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-933012e |
|-----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 20.9 ms                                                                | 20.0 ms: 1.04x faster                                                       |
| django_template | 33.2 ms                                                                | 32.3 ms: 1.03x faster                                                       |
| genshi_xml      | 47.0 ms                                                                | 46.0 ms: 1.02x faster                                                       |
| mako            | 9.64 ms                                                                | 9.50 ms: 1.02x faster                                                       |
| Geometric mean  | (ref)                                                                  | 1.03x faster                                                                |

All benchmarks:
===============

| Benchmark               | bm-20230201-linux-x86_64-python-95fb0e02582b5673eff4-3.12.0a4+-95fb0e0 | bm-20230118-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-933012e |
|-------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mdp                     | 2.70 sec                                                               | 2.44 sec: 1.10x faster                                                      |
| genshi_text             | 20.9 ms                                                                | 20.0 ms: 1.04x faster                                                       |
| gc_traversal            | 3.65 ms                                                                | 3.51 ms: 1.04x faster                                                       |
| go                      | 137 ms                                                                 | 134 ms: 1.03x faster                                                        |
| django_template         | 33.2 ms                                                                | 32.3 ms: 1.03x faster                                                       |
| scimark_sparse_mat_mult | 4.07 ms                                                                | 3.96 ms: 1.03x faster                                                       |
| logging_silent          | 92.8 ns                                                                | 90.4 ns: 1.03x faster                                                       |
| genshi_xml              | 47.0 ms                                                                | 46.0 ms: 1.02x faster                                                       |
| unpickle_pure_python    | 200 us                                                                 | 196 us: 1.02x faster                                                        |
| json_dumps              | 9.52 ms                                                                | 9.32 ms: 1.02x faster                                                       |
| nbody                   | 96.0 ms                                                                | 94.1 ms: 1.02x faster                                                       |
| logging_simple          | 5.73 us                                                                | 5.62 us: 1.02x faster                                                       |
| meteor_contest          | 105 ms                                                                 | 103 ms: 1.02x faster                                                        |
| pidigits                | 193 ms                                                                 | 189 ms: 1.02x faster                                                        |
| pickle_pure_python      | 285 us                                                                 | 280 us: 1.02x faster                                                        |
| deepcopy_memo           | 34.9 us                                                                | 34.4 us: 1.02x faster                                                       |
| mako                    | 9.64 ms                                                                | 9.50 ms: 1.02x faster                                                       |
| pycparser               | 1.10 sec                                                               | 1.08 sec: 1.02x faster                                                      |
| pprint_pformat          | 1.39 sec                                                               | 1.37 sec: 1.01x faster                                                      |
| python_startup_no_site  | 6.48 ms                                                                | 6.39 ms: 1.01x faster                                                       |
| generators              | 77.0 ms                                                                | 76.0 ms: 1.01x faster                                                       |
| logging_format          | 6.26 us                                                                | 6.18 us: 1.01x faster                                                       |
| chaos                   | 64.0 ms                                                                | 63.3 ms: 1.01x faster                                                       |
| python_startup          | 8.95 ms                                                                | 8.85 ms: 1.01x faster                                                       |
| deepcopy                | 329 us                                                                 | 325 us: 1.01x faster                                                        |
| scimark_fft             | 305 ms                                                                 | 301 ms: 1.01x faster                                                        |
| pprint_safe_repr        | 677 ms                                                                 | 670 ms: 1.01x faster                                                        |
| deltablue               | 3.23 ms                                                                | 3.20 ms: 1.01x faster                                                       |
| scimark_sor             | 106 ms                                                                 | 105 ms: 1.01x faster                                                        |
| 2to3                    | 251 ms                                                                 | 249 ms: 1.01x faster                                                        |
| async_generators        | 352 ms                                                                 | 349 ms: 1.01x faster                                                        |
| fannkuch                | 365 ms                                                                 | 362 ms: 1.01x faster                                                        |
| pathlib                 | 17.8 ms                                                                | 17.7 ms: 1.01x faster                                                       |
| json_loads              | 24.2 us                                                                | 24.1 us: 1.01x faster                                                       |
| raytrace                | 285 ms                                                                 | 283 ms: 1.01x faster                                                        |
| richards                | 42.4 ms                                                                | 42.2 ms: 1.01x faster                                                       |
| chameleon               | 6.41 ms                                                                | 6.37 ms: 1.01x faster                                                       |
| sqlglot_transpile       | 1.71 ms                                                                | 1.70 ms: 1.01x faster                                                       |
| create_gc_cycles        | 1.47 ms                                                                | 1.46 ms: 1.00x faster                                                       |
| sqlglot_parse           | 1.41 ms                                                                | 1.41 ms: 1.00x faster                                                       |
| hexiom                  | 5.99 ms                                                                | 5.96 ms: 1.00x faster                                                       |
| asyncio_tcp             | 495 ms                                                                 | 497 ms: 1.00x slower                                                        |
| sqlglot_optimize        | 51.2 ms                                                                | 51.4 ms: 1.01x slower                                                       |
| tornado_http            | 93.7 ms                                                                | 94.3 ms: 1.01x slower                                                       |
| xml_etree_parse         | 147 ms                                                                 | 148 ms: 1.01x slower                                                        |
| sqlglot_normalize       | 106 ms                                                                 | 106 ms: 1.01x slower                                                        |
| async_tree_io           | 1.31 sec                                                               | 1.32 sec: 1.01x slower                                                      |
| dulwich_log             | 62.4 ms                                                                | 62.9 ms: 1.01x slower                                                       |
| pickle                  | 10.1 us                                                                | 10.2 us: 1.01x slower                                                       |
| xml_etree_iterparse     | 101 ms                                                                 | 102 ms: 1.01x slower                                                        |
| xml_etree_process       | 53.4 ms                                                                | 54.1 ms: 1.01x slower                                                       |
| pyflate                 | 394 ms                                                                 | 399 ms: 1.01x slower                                                        |
| crypto_pyaes            | 73.0 ms                                                                | 74.1 ms: 1.02x slower                                                       |
| unpickle_list           | 5.01 us                                                                | 5.09 us: 1.02x slower                                                       |
| xml_etree_generate      | 77.1 ms                                                                | 78.5 ms: 1.02x slower                                                       |
| coverage                | 94.3 ms                                                                | 96.1 ms: 1.02x slower                                                       |
| pickle_dict             | 31.0 us                                                                | 31.6 us: 1.02x slower                                                       |
| nqueens                 | 75.0 ms                                                                | 77.2 ms: 1.03x slower                                                       |
| regex_dna               | 201 ms                                                                 | 207 ms: 1.03x slower                                                        |
| spectral_norm           | 94.3 ms                                                                | 97.4 ms: 1.03x slower                                                       |
| coroutines              | 25.0 ms                                                                | 26.0 ms: 1.04x slower                                                       |
| regex_effbot            | 3.36 ms                                                                | 3.51 ms: 1.04x slower                                                       |
| unpickle                | 13.3 us                                                                | 14.0 us: 1.05x slower                                                       |
| Geometric mean          | (ref)                                                                  | 1.00x faster                                                                |

Benchmark hidden because not significant (28): djangocms, html5lib, sympy_expand, float, json, deepcopy_reduce, thrift, dask, sympy_integrate, sqlite_synth, gunicorn, mypy, docutils, bench_thread_pool, async_tree_cpu_io_mixed, async_tree_none, bench_mp_pool, aiohttp, pickle_list, regex_compile, sympy_str, sympy_sum, regex_v8, scimark_monte_carlo, unpack_sequence, scimark_lu, telco, async_tree_memoization
