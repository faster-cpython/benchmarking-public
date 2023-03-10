
# Results vs. base

- fork: faster-cpython
- ref: specialize_calls_to_
- machine: linux-x86_64
- commit hash: b851a2a
- commit date: 2023-03-09
- overall geometric mean: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230309-linux-x86_64-python-b45d14b88611fefc6f05-3.12.0a6+-b45d14b | bm-20230309-linux-x86_64-faster%2dcpython-specialize_calls_to_-3.12.0a6+-b851a2a |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| chameleon      | 6.49 ms                                                                | 6.67 ms: 1.03x slower                                                            |
| docutils       | 2.57 sec                                                               | 2.55 sec: 1.01x faster                                                           |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                                     |

Benchmark hidden because not significant (3): 2to3, html5lib, tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230309-linux-x86_64-python-b45d14b88611fefc6f05-3.12.0a6+-b45d14b | bm-20230309-linux-x86_64-faster%2dcpython-specialize_calls_to_-3.12.0a6+-b851a2a |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| float          | 74.7 ms                                                                | 74.1 ms: 1.01x faster                                                            |
| pidigits       | 190 ms                                                                 | 189 ms: 1.00x faster                                                             |
| nbody          | 88.8 ms                                                                | 94.0 ms: 1.06x slower                                                            |
| Geometric mean | (ref)                                                                  | 1.02x slower                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230309-linux-x86_64-python-b45d14b88611fefc6f05-3.12.0a6+-b45d14b | bm-20230309-linux-x86_64-faster%2dcpython-specialize_calls_to_-3.12.0a6+-b851a2a |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_effbot   | 3.51 ms                                                                | 3.37 ms: 1.04x faster                                                            |
| regex_dna      | 209 ms                                                                 | 205 ms: 1.02x faster                                                             |
| regex_v8       | 21.9 ms                                                                | 21.5 ms: 1.02x faster                                                            |
| regex_compile  | 134 ms                                                                 | 134 ms: 1.00x slower                                                             |
| Geometric mean | (ref)                                                                  | 1.02x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230309-linux-x86_64-python-b45d14b88611fefc6f05-3.12.0a6+-b45d14b | bm-20230309-linux-x86_64-faster%2dcpython-specialize_calls_to_-3.12.0a6+-b851a2a |
|----------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| unpickle_pure_python | 206 us                                                                 | 200 us: 1.03x faster                                                             |
| pickle_list          | 4.30 us                                                                | 4.25 us: 1.01x faster                                                            |
| xml_etree_generate   | 81.9 ms                                                                | 81.2 ms: 1.01x faster                                                            |
| json_dumps           | 9.54 ms                                                                | 9.47 ms: 1.01x faster                                                            |
| json_loads           | 24.3 us                                                                | 24.1 us: 1.01x faster                                                            |
| pickle_dict          | 31.7 us                                                                | 31.6 us: 1.00x faster                                                            |
| xml_etree_iterparse  | 99.7 ms                                                                | 100 ms: 1.01x slower                                                             |
| unpickle_list        | 4.96 us                                                                | 5.00 us: 1.01x slower                                                            |
| pickle               | 10.4 us                                                                | 10.5 us: 1.01x slower                                                            |
| Geometric mean       | (ref)                                                                  | 1.00x faster                                                                     |

Benchmark hidden because not significant (4): xml_etree_process, xml_etree_parse, pickle_pure_python, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230309-linux-x86_64-python-b45d14b88611fefc6f05-3.12.0a6+-b45d14b | bm-20230309-linux-x86_64-faster%2dcpython-specialize_calls_to_-3.12.0a6+-b851a2a |
|------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 6.58 ms                                                                | 6.54 ms: 1.01x faster                                                            |
| python_startup         | 9.07 ms                                                                | 9.03 ms: 1.00x faster                                                            |
| Geometric mean         | (ref)                                                                  | 1.00x faster                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20230309-linux-x86_64-python-b45d14b88611fefc6f05-3.12.0a6+-b45d14b | bm-20230309-linux-x86_64-faster%2dcpython-specialize_calls_to_-3.12.0a6+-b851a2a |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mako           | 10.1 ms                                                                | 10.0 ms: 1.01x faster                                                            |
| genshi_xml     | 48.4 ms                                                                | 48.2 ms: 1.01x faster                                                            |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                                     |

Benchmark hidden because not significant (2): genshi_text, django_template

All benchmarks:
===============

| Benchmark               | bm-20230309-linux-x86_64-python-b45d14b88611fefc6f05-3.12.0a6+-b45d14b | bm-20230309-linux-x86_64-faster%2dcpython-specialize_calls_to_-3.12.0a6+-b851a2a |
|-------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| raytrace                | 289 ms                                                                 | 267 ms: 1.08x faster                                                             |
| chaos                   | 69.5 ms                                                                | 65.4 ms: 1.06x faster                                                            |
| unpack_sequence         | 43.9 ns                                                                | 41.5 ns: 1.06x faster                                                            |
| regex_effbot            | 3.51 ms                                                                | 3.37 ms: 1.04x faster                                                            |
| coverage                | 98.0 ms                                                                | 95.1 ms: 1.03x faster                                                            |
| scimark_fft             | 325 ms                                                                 | 315 ms: 1.03x faster                                                             |
| unpickle_pure_python    | 206 us                                                                 | 200 us: 1.03x faster                                                             |
| scimark_monte_carlo     | 68.6 ms                                                                | 66.8 ms: 1.03x faster                                                            |
| comprehensions          | 24.3 us                                                                | 23.7 us: 1.02x faster                                                            |
| scimark_lu              | 113 ms                                                                 | 110 ms: 1.02x faster                                                             |
| regex_dna               | 209 ms                                                                 | 205 ms: 1.02x faster                                                             |
| regex_v8                | 21.9 ms                                                                | 21.5 ms: 1.02x faster                                                            |
| deltablue               | 3.27 ms                                                                | 3.21 ms: 1.02x faster                                                            |
| deepcopy                | 339 us                                                                 | 334 us: 1.02x faster                                                             |
| sqlglot_parse           | 1.46 ms                                                                | 1.44 ms: 1.02x faster                                                            |
| async_generators        | 409 ms                                                                 | 403 ms: 1.01x faster                                                             |
| json                    | 4.68 ms                                                                | 4.62 ms: 1.01x faster                                                            |
| generators              | 30.7 ms                                                                | 30.3 ms: 1.01x faster                                                            |
| sqlglot_transpile       | 1.75 ms                                                                | 1.73 ms: 1.01x faster                                                            |
| nqueens                 | 81.4 ms                                                                | 80.3 ms: 1.01x faster                                                            |
| deepcopy_memo           | 34.4 us                                                                | 34.0 us: 1.01x faster                                                            |
| sqlalchemy_declarative  | 139 ms                                                                 | 137 ms: 1.01x faster                                                             |
| scimark_sor             | 108 ms                                                                 | 107 ms: 1.01x faster                                                             |
| sympy_expand            | 468 ms                                                                 | 462 ms: 1.01x faster                                                             |
| pickle_list             | 4.30 us                                                                | 4.25 us: 1.01x faster                                                            |
| xml_etree_generate      | 81.9 ms                                                                | 81.2 ms: 1.01x faster                                                            |
| logging_simple          | 5.84 us                                                                | 5.79 us: 1.01x faster                                                            |
| coroutines              | 23.2 ms                                                                | 23.0 ms: 1.01x faster                                                            |
| logging_silent          | 95.4 ns                                                                | 94.6 ns: 1.01x faster                                                            |
| json_dumps              | 9.54 ms                                                                | 9.47 ms: 1.01x faster                                                            |
| float                   | 74.7 ms                                                                | 74.1 ms: 1.01x faster                                                            |
| mako                    | 10.1 ms                                                                | 10.0 ms: 1.01x faster                                                            |
| bench_thread_pool       | 796 us                                                                 | 790 us: 1.01x faster                                                             |
| docutils                | 2.57 sec                                                               | 2.55 sec: 1.01x faster                                                           |
| richards                | 43.8 ms                                                                | 43.5 ms: 1.01x faster                                                            |
| mypy2                   | 335 ms                                                                 | 333 ms: 1.01x faster                                                             |
| sympy_integrate         | 20.8 ms                                                                | 20.6 ms: 1.01x faster                                                            |
| json_loads              | 24.3 us                                                                | 24.1 us: 1.01x faster                                                            |
| aiohttp                 | 1.02 ms                                                                | 1.01 ms: 1.01x faster                                                            |
| genshi_xml              | 48.4 ms                                                                | 48.2 ms: 1.01x faster                                                            |
| sympy_str               | 288 ms                                                                 | 287 ms: 1.01x faster                                                             |
| sympy_sum               | 169 ms                                                                 | 168 ms: 1.01x faster                                                             |
| python_startup_no_site  | 6.58 ms                                                                | 6.54 ms: 1.01x faster                                                            |
| gunicorn                | 1.10 ms                                                                | 1.09 ms: 1.01x faster                                                            |
| python_startup          | 9.07 ms                                                                | 9.03 ms: 1.00x faster                                                            |
| pickle_dict             | 31.7 us                                                                | 31.6 us: 1.00x faster                                                            |
| dulwich_log             | 64.2 ms                                                                | 63.9 ms: 1.00x faster                                                            |
| sqlglot_normalize       | 105 ms                                                                 | 104 ms: 1.00x faster                                                             |
| sqlglot_optimize        | 51.3 ms                                                                | 51.2 ms: 1.00x faster                                                            |
| pidigits                | 190 ms                                                                 | 189 ms: 1.00x faster                                                             |
| regex_compile           | 134 ms                                                                 | 134 ms: 1.00x slower                                                             |
| xml_etree_iterparse     | 99.7 ms                                                                | 100 ms: 1.01x slower                                                             |
| thrift                  | 784 us                                                                 | 790 us: 1.01x slower                                                             |
| unpickle_list           | 4.96 us                                                                | 5.00 us: 1.01x slower                                                            |
| crypto_pyaes            | 74.0 ms                                                                | 74.7 ms: 1.01x slower                                                            |
| sqlite_synth            | 2.61 us                                                                | 2.64 us: 1.01x slower                                                            |
| spectral_norm           | 95.9 ms                                                                | 96.9 ms: 1.01x slower                                                            |
| pickle                  | 10.4 us                                                                | 10.5 us: 1.01x slower                                                            |
| pyflate                 | 406 ms                                                                 | 411 ms: 1.01x slower                                                             |
| async_tree_io           | 1.29 sec                                                               | 1.31 sec: 1.01x slower                                                           |
| deepcopy_reduce         | 2.97 us                                                                | 3.01 us: 1.01x slower                                                            |
| meteor_contest          | 103 ms                                                                 | 105 ms: 1.02x slower                                                             |
| fannkuch                | 364 ms                                                                 | 373 ms: 1.02x slower                                                             |
| chameleon               | 6.49 ms                                                                | 6.67 ms: 1.03x slower                                                            |
| mdp                     | 2.40 sec                                                               | 2.48 sec: 1.03x slower                                                           |
| scimark_sparse_mat_mult | 4.45 ms                                                                | 4.62 ms: 1.04x slower                                                            |
| nbody                   | 88.8 ms                                                                | 94.0 ms: 1.06x slower                                                            |
| gc_traversal            | 3.61 ms                                                                | 3.85 ms: 1.07x slower                                                            |
| Geometric mean          | (ref)                                                                  | 1.00x faster                                                                     |

Benchmark hidden because not significant (26): html5lib, dask, pycparser, logging_format, pprint_pformat, telco, go, pprint_safe_repr, pathlib, create_gc_cycles, xml_etree_process, xml_etree_parse, genshi_text, pickle_pure_python, 2to3, async_tree_none, bench_mp_pool, hexiom, asyncio_tcp, django_template, tornado_http, async_tree_cpu_io_mixed, sqlalchemy_imperative, async_tree_memoization, djangocms, unpickle
