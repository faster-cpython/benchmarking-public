
# Results vs. base

- fork: faster-cpython
- ref: safe_decref
- machine: linux-x86_64
- commit hash: b17c8ef
- commit date: 2023-06-03
- overall geometric mean: 1.01x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230605-linux-x86_64-python-06893403668961fdbd5d-3.13.0a0-0689340 | bm-20230603-linux-x86_64-faster%2dcpython-safe_decref-3.13.0a0-b17c8ef |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| tornado_http   | 96.2 ms                                                               | 95.5 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                           |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230605-linux-x86_64-python-06893403668961fdbd5d-3.13.0a0-0689340 | bm-20230603-linux-x86_64-faster%2dcpython-safe_decref-3.13.0a0-b17c8ef |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| pidigits       | 197 ms                                                                | 189 ms: 1.04x faster                                                   |
| float          | 79.4 ms                                                               | 76.6 ms: 1.04x faster                                                  |
| Geometric mean | (ref)                                                                 | 1.02x faster                                                           |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230605-linux-x86_64-python-06893403668961fdbd5d-3.13.0a0-0689340 | bm-20230603-linux-x86_64-faster%2dcpython-safe_decref-3.13.0a0-b17c8ef |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                                | 136 ms: 1.01x faster                                                   |
| regex_dna      | 207 ms                                                                | 214 ms: 1.03x slower                                                   |
| regex_effbot   | 3.58 ms                                                               | 3.71 ms: 1.04x slower                                                  |
| regex_v8       | 22.0 ms                                                               | 22.9 ms: 1.04x slower                                                  |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230605-linux-x86_64-python-06893403668961fdbd5d-3.13.0a0-0689340 | bm-20230603-linux-x86_64-faster%2dcpython-safe_decref-3.13.0a0-b17c8ef |
|----------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_dict          | 31.8 us                                                               | 30.4 us: 1.04x faster                                                  |
| pickle_list          | 4.70 us                                                               | 4.57 us: 1.03x faster                                                  |
| pickle_pure_python   | 314 us                                                                | 308 us: 1.02x faster                                                   |
| pickle               | 10.8 us                                                               | 10.6 us: 1.02x faster                                                  |
| json_dumps           | 9.81 ms                                                               | 9.67 ms: 1.01x faster                                                  |
| xml_etree_process    | 57.5 ms                                                               | 57.0 ms: 1.01x faster                                                  |
| unpickle             | 15.1 us                                                               | 15.0 us: 1.01x faster                                                  |
| tomli_loads          | 2.17 sec                                                              | 2.15 sec: 1.01x faster                                                 |
| xml_etree_generate   | 84.0 ms                                                               | 83.5 ms: 1.01x faster                                                  |
| unpickle_pure_python | 216 us                                                                | 215 us: 1.00x faster                                                   |
| Geometric mean       | (ref)                                                                 | 1.01x faster                                                           |

Benchmark hidden because not significant (4): xml_etree_iterparse, unpickle_list, json_loads, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230605-linux-x86_64-python-06893403668961fdbd5d-3.13.0a0-0689340 | bm-20230603-linux-x86_64-faster%2dcpython-safe_decref-3.13.0a0-b17c8ef |
|------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 6.65 ms                                                               | 6.69 ms: 1.01x slower                                                  |
| python_startup         | 9.13 ms                                                               | 9.21 ms: 1.01x slower                                                  |
| Geometric mean         | (ref)                                                                 | 1.01x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20230605-linux-x86_64-python-06893403668961fdbd5d-3.13.0a0-0689340 | bm-20230603-linux-x86_64-faster%2dcpython-safe_decref-3.13.0a0-b17c8ef |
|-----------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako      | 10.6 ms                                                               | 10.6 ms: 1.01x faster                                                  |

All benchmarks:
===============

| Benchmark                | bm-20230605-linux-x86_64-python-06893403668961fdbd5d-3.13.0a0-0689340 | bm-20230603-linux-x86_64-faster%2dcpython-safe_decref-3.13.0a0-b17c8ef |
|--------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| unpack_sequence          | 52.7 ns                                                               | 44.4 ns: 1.19x faster                                                  |
| scimark_sparse_mat_mult  | 5.21 ms                                                               | 4.71 ms: 1.11x faster                                                  |
| pickle_dict              | 31.8 us                                                               | 30.4 us: 1.04x faster                                                  |
| pidigits                 | 197 ms                                                                | 189 ms: 1.04x faster                                                   |
| float                    | 79.4 ms                                                               | 76.6 ms: 1.04x faster                                                  |
| pycparser                | 1.18 sec                                                              | 1.14 sec: 1.04x faster                                                 |
| scimark_lu               | 112 ms                                                                | 108 ms: 1.04x faster                                                   |
| logging_silent           | 98.0 ns                                                               | 94.9 ns: 1.03x faster                                                  |
| pickle_list              | 4.70 us                                                               | 4.57 us: 1.03x faster                                                  |
| typing_runtime_protocols | 144 us                                                                | 141 us: 1.02x faster                                                   |
| sqlglot_parse            | 1.31 ms                                                               | 1.28 ms: 1.02x faster                                                  |
| pprint_pformat           | 1.49 sec                                                              | 1.46 sec: 1.02x faster                                                 |
| sqlglot_transpile        | 1.63 ms                                                               | 1.60 ms: 1.02x faster                                                  |
| pickle_pure_python       | 314 us                                                                | 308 us: 1.02x faster                                                   |
| pprint_safe_repr         | 732 ms                                                                | 720 ms: 1.02x faster                                                   |
| scimark_fft              | 353 ms                                                                | 348 ms: 1.02x faster                                                   |
| pickle                   | 10.8 us                                                               | 10.6 us: 1.02x faster                                                  |
| fannkuch                 | 394 ms                                                                | 388 ms: 1.02x faster                                                   |
| scimark_sor              | 119 ms                                                                | 117 ms: 1.01x faster                                                   |
| json_dumps               | 9.81 ms                                                               | 9.67 ms: 1.01x faster                                                  |
| crypto_pyaes             | 77.9 ms                                                               | 76.8 ms: 1.01x faster                                                  |
| deltablue                | 3.24 ms                                                               | 3.20 ms: 1.01x faster                                                  |
| pathlib                  | 18.6 ms                                                               | 18.3 ms: 1.01x faster                                                  |
| deepcopy                 | 354 us                                                                | 350 us: 1.01x faster                                                   |
| scimark_monte_carlo      | 71.2 ms                                                               | 70.4 ms: 1.01x faster                                                  |
| dask                     | 517 ms                                                                | 512 ms: 1.01x faster                                                   |
| xml_etree_process        | 57.5 ms                                                               | 57.0 ms: 1.01x faster                                                  |
| unpickle                 | 15.1 us                                                               | 15.0 us: 1.01x faster                                                  |
| tornado_http             | 96.2 ms                                                               | 95.5 ms: 1.01x faster                                                  |
| go                       | 134 ms                                                                | 133 ms: 1.01x faster                                                   |
| regex_compile            | 137 ms                                                                | 136 ms: 1.01x faster                                                   |
| deepcopy_reduce          | 3.18 us                                                               | 3.16 us: 1.01x faster                                                  |
| tomli_loads              | 2.17 sec                                                              | 2.15 sec: 1.01x faster                                                 |
| xml_etree_generate       | 84.0 ms                                                               | 83.5 ms: 1.01x faster                                                  |
| sqlglot_normalize        | 105 ms                                                                | 105 ms: 1.01x faster                                                   |
| mako                     | 10.6 ms                                                               | 10.6 ms: 1.01x faster                                                  |
| mypy2                    | 336 ms                                                                | 335 ms: 1.01x faster                                                   |
| raytrace                 | 290 ms                                                                | 288 ms: 1.00x faster                                                   |
| sqlglot_optimize         | 52.6 ms                                                               | 52.4 ms: 1.00x faster                                                  |
| unpickle_pure_python     | 216 us                                                                | 215 us: 1.00x faster                                                   |
| asyncio_tcp_ssl          | 1.79 sec                                                              | 1.79 sec: 1.00x faster                                                 |
| async_tree_io            | 1.22 sec                                                              | 1.22 sec: 1.00x faster                                                 |
| mdp                      | 2.68 sec                                                              | 2.68 sec: 1.00x faster                                                 |
| python_startup_no_site   | 6.65 ms                                                               | 6.69 ms: 1.01x slower                                                  |
| python_startup           | 9.13 ms                                                               | 9.21 ms: 1.01x slower                                                  |
| coroutines               | 22.5 ms                                                               | 22.7 ms: 1.01x slower                                                  |
| meteor_contest           | 105 ms                                                                | 106 ms: 1.01x slower                                                   |
| async_generators         | 441 ms                                                                | 446 ms: 1.01x slower                                                   |
| coverage                 | 93.4 ms                                                               | 95.5 ms: 1.02x slower                                                  |
| logging_simple           | 5.93 us                                                               | 6.08 us: 1.02x slower                                                  |
| telco                    | 6.77 ms                                                               | 6.96 ms: 1.03x slower                                                  |
| regex_dna                | 207 ms                                                                | 214 ms: 1.03x slower                                                   |
| regex_effbot             | 3.58 ms                                                               | 3.71 ms: 1.04x slower                                                  |
| regex_v8                 | 22.0 ms                                                               | 22.9 ms: 1.04x slower                                                  |
| Geometric mean           | (ref)                                                                 | 1.01x faster                                                           |

Benchmark hidden because not significant (28): json, async_tree_none, async_tree_cpu_io_mixed, xml_etree_iterparse, docutils, generators, richards_super, comprehensions, async_tree_memoization, dulwich_log, deepcopy_memo, spectral_norm, chaos, unpickle_list, bench_thread_pool, hexiom, pyflate, gc_traversal, bench_mp_pool, create_gc_cycles, asyncio_tcp, json_loads, nqueens, logging_format, sqlite_synth, nbody, xml_etree_parse, richards
