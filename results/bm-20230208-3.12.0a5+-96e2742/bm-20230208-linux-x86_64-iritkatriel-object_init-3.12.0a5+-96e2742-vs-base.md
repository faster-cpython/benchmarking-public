
# Results vs. base

- fork: iritkatriel
- ref: object_init
- machine: linux-x86_64
- commit hash: 96e2742
- commit date: 2023-02-08
- overall geometric mean: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230208-linux-x86_64-python-eb49d32b9af0b3b01a55-3.12.0a5+-eb49d32 | bm-20230208-linux-x86_64-iritkatriel-object_init-3.12.0a5+-96e2742 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 251 ms                                                                 | 251 ms: 1.00x slower                                               |
| chameleon      | 6.37 ms                                                                | 6.48 ms: 1.02x slower                                              |
| docutils       | 2.53 sec                                                               | 2.55 sec: 1.01x slower                                             |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                       |

Benchmark hidden because not significant (2): html5lib, tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230208-linux-x86_64-python-eb49d32b9af0b3b01a55-3.12.0a5+-eb49d32 | bm-20230208-linux-x86_64-iritkatriel-object_init-3.12.0a5+-96e2742 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| nbody          | 94.3 ms                                                                | 86.6 ms: 1.09x faster                                              |
| pidigits       | 193 ms                                                                 | 189 ms: 1.02x faster                                               |
| float          | 72.9 ms                                                                | 71.8 ms: 1.01x faster                                              |
| Geometric mean | (ref)                                                                  | 1.04x faster                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230208-linux-x86_64-python-eb49d32b9af0b3b01a55-3.12.0a5+-eb49d32 | bm-20230208-linux-x86_64-iritkatriel-object_init-3.12.0a5+-96e2742 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_dna      | 219 ms                                                                 | 211 ms: 1.04x faster                                               |
| regex_compile  | 128 ms                                                                 | 128 ms: 1.00x slower                                               |
| regex_effbot   | 3.36 ms                                                                | 3.40 ms: 1.01x slower                                              |
| regex_v8       | 21.5 ms                                                                | 21.7 ms: 1.01x slower                                              |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230208-linux-x86_64-python-eb49d32b9af0b3b01a55-3.12.0a5+-eb49d32 | bm-20230208-linux-x86_64-iritkatriel-object_init-3.12.0a5+-96e2742 |
|----------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| json_dumps           | 9.51 ms                                                                | 9.44 ms: 1.01x faster                                              |
| xml_etree_process    | 55.8 ms                                                                | 55.4 ms: 1.01x faster                                              |
| xml_etree_generate   | 80.3 ms                                                                | 80.0 ms: 1.00x faster                                              |
| pickle_dict          | 30.8 us                                                                | 31.0 us: 1.01x slower                                              |
| pickle_pure_python   | 286 us                                                                 | 289 us: 1.01x slower                                               |
| json_loads           | 23.5 us                                                                | 23.8 us: 1.01x slower                                              |
| unpickle_pure_python | 196 us                                                                 | 199 us: 1.01x slower                                               |
| unpickle_list        | 4.90 us                                                                | 4.97 us: 1.02x slower                                              |
| pickle               | 9.99 us                                                                | 10.2 us: 1.02x slower                                              |
| unpickle             | 12.9 us                                                                | 13.1 us: 1.02x slower                                              |
| xml_etree_iterparse  | 103 ms                                                                 | 107 ms: 1.04x slower                                               |
| Geometric mean       | (ref)                                                                  | 1.01x slower                                                       |

Benchmark hidden because not significant (2): xml_etree_parse, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230208-linux-x86_64-python-eb49d32b9af0b3b01a55-3.12.0a5+-eb49d32 | bm-20230208-linux-x86_64-iritkatriel-object_init-3.12.0a5+-96e2742 |
|------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup_no_site | 6.46 ms                                                                | 6.45 ms: 1.00x faster                                              |
| python_startup         | 8.90 ms                                                                | 8.90 ms: 1.00x faster                                              |
| Geometric mean         | (ref)                                                                  | 1.00x faster                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20230208-linux-x86_64-python-eb49d32b9af0b3b01a55-3.12.0a5+-eb49d32 | bm-20230208-linux-x86_64-iritkatriel-object_init-3.12.0a5+-96e2742 |
|-----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| genshi_text     | 20.8 ms                                                                | 20.5 ms: 1.01x faster                                              |
| genshi_xml      | 46.9 ms                                                                | 46.3 ms: 1.01x faster                                              |
| django_template | 32.7 ms                                                                | 32.5 ms: 1.01x faster                                              |
| Geometric mean  | (ref)                                                                  | 1.01x faster                                                       |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark               | bm-20230208-linux-x86_64-python-eb49d32b9af0b3b01a55-3.12.0a5+-eb49d32 | bm-20230208-linux-x86_64-iritkatriel-object_init-3.12.0a5+-96e2742 |
|-------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| nbody                   | 94.3 ms                                                                | 86.6 ms: 1.09x faster                                              |
| deepcopy_reduce         | 3.01 us                                                                | 2.89 us: 1.04x faster                                              |
| gc_traversal            | 3.79 ms                                                                | 3.65 ms: 1.04x faster                                              |
| regex_dna               | 219 ms                                                                 | 211 ms: 1.04x faster                                               |
| scimark_sparse_mat_mult | 4.03 ms                                                                | 3.91 ms: 1.03x faster                                              |
| json                    | 4.69 ms                                                                | 4.56 ms: 1.03x faster                                              |
| scimark_fft             | 307 ms                                                                 | 298 ms: 1.03x faster                                               |
| raytrace                | 288 ms                                                                 | 282 ms: 1.02x faster                                               |
| chaos                   | 65.8 ms                                                                | 64.3 ms: 1.02x faster                                              |
| pathlib                 | 17.9 ms                                                                | 17.5 ms: 1.02x faster                                              |
| pprint_safe_repr        | 689 ms                                                                 | 674 ms: 1.02x faster                                               |
| pidigits                | 193 ms                                                                 | 189 ms: 1.02x faster                                               |
| spectral_norm           | 96.0 ms                                                                | 94.3 ms: 1.02x faster                                              |
| float                   | 72.9 ms                                                                | 71.8 ms: 1.01x faster                                              |
| deepcopy                | 332 us                                                                 | 327 us: 1.01x faster                                               |
| sqlglot_normalize       | 106 ms                                                                 | 105 ms: 1.01x faster                                               |
| pprint_pformat          | 1.40 sec                                                               | 1.38 sec: 1.01x faster                                             |
| genshi_text             | 20.8 ms                                                                | 20.5 ms: 1.01x faster                                              |
| coroutines              | 25.5 ms                                                                | 25.2 ms: 1.01x faster                                              |
| genshi_xml              | 46.9 ms                                                                | 46.3 ms: 1.01x faster                                              |
| scimark_monte_carlo     | 66.4 ms                                                                | 65.8 ms: 1.01x faster                                              |
| json_dumps              | 9.51 ms                                                                | 9.44 ms: 1.01x faster                                              |
| django_template         | 32.7 ms                                                                | 32.5 ms: 1.01x faster                                              |
| deltablue               | 3.21 ms                                                                | 3.19 ms: 1.01x faster                                              |
| create_gc_cycles        | 1.46 ms                                                                | 1.45 ms: 1.01x faster                                              |
| xml_etree_process       | 55.8 ms                                                                | 55.4 ms: 1.01x faster                                              |
| sqlglot_optimize        | 51.4 ms                                                                | 51.1 ms: 1.01x faster                                              |
| aiohttp                 | 1.01 ms                                                                | 1.00 ms: 1.01x faster                                              |
| xml_etree_generate      | 80.3 ms                                                                | 80.0 ms: 1.00x faster                                              |
| dulwich_log             | 63.1 ms                                                                | 62.9 ms: 1.00x faster                                              |
| asyncio_tcp             | 494 ms                                                                 | 493 ms: 1.00x faster                                               |
| bench_thread_pool       | 786 us                                                                 | 784 us: 1.00x faster                                               |
| python_startup_no_site  | 6.46 ms                                                                | 6.45 ms: 1.00x faster                                              |
| python_startup          | 8.90 ms                                                                | 8.90 ms: 1.00x faster                                              |
| 2to3                    | 251 ms                                                                 | 251 ms: 1.00x slower                                               |
| sympy_integrate         | 19.8 ms                                                                | 19.9 ms: 1.00x slower                                              |
| regex_compile           | 128 ms                                                                 | 128 ms: 1.00x slower                                               |
| sympy_sum               | 158 ms                                                                 | 158 ms: 1.00x slower                                               |
| docutils                | 2.53 sec                                                               | 2.55 sec: 1.01x slower                                             |
| pickle_dict             | 30.8 us                                                                | 31.0 us: 1.01x slower                                              |
| pyflate                 | 400 ms                                                                 | 403 ms: 1.01x slower                                               |
| go                      | 134 ms                                                                 | 135 ms: 1.01x slower                                               |
| pickle_pure_python      | 286 us                                                                 | 289 us: 1.01x slower                                               |
| regex_effbot            | 3.36 ms                                                                | 3.40 ms: 1.01x slower                                              |
| hexiom                  | 5.93 ms                                                                | 6.00 ms: 1.01x slower                                              |
| regex_v8                | 21.5 ms                                                                | 21.7 ms: 1.01x slower                                              |
| sqlalchemy_declarative  | 136 ms                                                                 | 138 ms: 1.01x slower                                               |
| json_loads              | 23.5 us                                                                | 23.8 us: 1.01x slower                                              |
| unpickle_pure_python    | 196 us                                                                 | 199 us: 1.01x slower                                               |
| nqueens                 | 77.7 ms                                                                | 78.9 ms: 1.01x slower                                              |
| unpickle_list           | 4.90 us                                                                | 4.97 us: 1.02x slower                                              |
| pickle                  | 9.99 us                                                                | 10.2 us: 1.02x slower                                              |
| async_generators        | 424 ms                                                                 | 431 ms: 1.02x slower                                               |
| chameleon               | 6.37 ms                                                                | 6.48 ms: 1.02x slower                                              |
| unpickle                | 12.9 us                                                                | 13.1 us: 1.02x slower                                              |
| fannkuch                | 374 ms                                                                 | 382 ms: 1.02x slower                                               |
| meteor_contest          | 105 ms                                                                 | 108 ms: 1.03x slower                                               |
| unpack_sequence         | 43.2 ns                                                                | 44.6 ns: 1.03x slower                                              |
| xml_etree_iterparse     | 103 ms                                                                 | 107 ms: 1.04x slower                                               |
| generators              | 75.2 ms                                                                | 78.2 ms: 1.04x slower                                              |
| mdp                     | 2.53 sec                                                               | 2.66 sec: 1.05x slower                                             |
| Geometric mean          | (ref)                                                                  | 1.00x faster                                                       |

Benchmark hidden because not significant (31): xml_etree_parse, async_tree_none, async_tree_io, html5lib, pickle_list, async_tree_cpu_io_mixed, tornado_http, scimark_lu, richards, sqlite_synth, sqlglot_parse, sympy_expand, sqlglot_transpile, bench_mp_pool, scimark_sor, crypto_pyaes, logging_format, deepcopy_memo, async_tree_memoization, sqlalchemy_imperative, sympy_str, mako, gunicorn, logging_simple, coverage, mypy2, logging_silent, pycparser, telco, thrift, djangocms
