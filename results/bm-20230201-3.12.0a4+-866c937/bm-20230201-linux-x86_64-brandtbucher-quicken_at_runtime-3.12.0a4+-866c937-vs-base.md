
# Results vs. base

- fork: brandtbucher
- ref: quicken_at_runtime
- machine: linux-x86_64
- commit hash: 866c937
- commit date: 2023-02-01
- overall geometric mean: 1.00x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230201-linux-x86_64-python-7840ff3cdbdf64f517c9-3.12.0a4+-7840ff3 | bm-20230201-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-866c937 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 254 ms                                                                 | 251 ms: 1.02x faster                                                       |
| docutils       | 2.51 sec                                                               | 2.50 sec: 1.00x faster                                                     |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                               |

Benchmark hidden because not significant (3): chameleon, html5lib, tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230201-linux-x86_64-python-7840ff3cdbdf64f517c9-3.12.0a4+-7840ff3 | bm-20230201-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-866c937 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 72.7 ms                                                                | 74.2 ms: 1.02x slower                                                      |
| pidigits       | 189 ms                                                                 | 198 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                                  | 1.02x slower                                                               |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230201-linux-x86_64-python-7840ff3cdbdf64f517c9-3.12.0a4+-7840ff3 | bm-20230201-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-866c937 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 22.6 ms                                                                | 22.4 ms: 1.01x faster                                                      |
| regex_dna      | 219 ms                                                                 | 217 ms: 1.01x faster                                                       |
| regex_compile  | 129 ms                                                                 | 128 ms: 1.01x faster                                                       |
| regex_effbot   | 3.61 ms                                                                | 3.76 ms: 1.04x slower                                                      |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230201-linux-x86_64-python-7840ff3cdbdf64f517c9-3.12.0a4+-7840ff3 | bm-20230201-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-866c937 |
|----------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| unpickle_list        | 5.10 us                                                                | 5.04 us: 1.01x faster                                                      |
| pickle_pure_python   | 285 us                                                                 | 283 us: 1.01x faster                                                       |
| json_loads           | 24.1 us                                                                | 24.3 us: 1.01x slower                                                      |
| xml_etree_parse      | 147 ms                                                                 | 148 ms: 1.01x slower                                                       |
| xml_etree_generate   | 77.3 ms                                                                | 78.0 ms: 1.01x slower                                                      |
| pickle               | 10.2 us                                                                | 10.3 us: 1.01x slower                                                      |
| unpickle_pure_python | 197 us                                                                 | 200 us: 1.02x slower                                                       |
| pickle_list          | 3.98 us                                                                | 4.25 us: 1.07x slower                                                      |
| pickle_dict          | 29.9 us                                                                | 32.4 us: 1.08x slower                                                      |
| Geometric mean       | (ref)                                                                  | 1.01x slower                                                               |

Benchmark hidden because not significant (4): unpickle, xml_etree_process, xml_etree_iterparse, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230201-linux-x86_64-python-7840ff3cdbdf64f517c9-3.12.0a4+-7840ff3 | bm-20230201-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-866c937 |
|------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 6.49 ms                                                                | 6.27 ms: 1.04x faster                                                      |
| python_startup         | 8.96 ms                                                                | 8.74 ms: 1.02x faster                                                      |
| Geometric mean         | (ref)                                                                  | 1.03x faster                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20230201-linux-x86_64-python-7840ff3cdbdf64f517c9-3.12.0a4+-7840ff3 | bm-20230201-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-866c937 |
|-----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_text     | 20.9 ms                                                                | 20.7 ms: 1.01x faster                                                      |
| genshi_xml      | 46.6 ms                                                                | 46.8 ms: 1.00x slower                                                      |
| django_template | 32.5 ms                                                                | 33.0 ms: 1.02x slower                                                      |
| mako            | 9.53 ms                                                                | 9.85 ms: 1.03x slower                                                      |
| Geometric mean  | (ref)                                                                  | 1.01x slower                                                               |

All benchmarks:
===============

| Benchmark               | bm-20230201-linux-x86_64-python-7840ff3cdbdf64f517c9-3.12.0a4+-7840ff3 | bm-20230201-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-866c937 |
|-------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site  | 6.49 ms                                                                | 6.27 ms: 1.04x faster                                                      |
| logging_silent          | 93.4 ns                                                                | 90.6 ns: 1.03x faster                                                      |
| python_startup          | 8.96 ms                                                                | 8.74 ms: 1.02x faster                                                      |
| deltablue               | 3.25 ms                                                                | 3.18 ms: 1.02x faster                                                      |
| fannkuch                | 369 ms                                                                 | 362 ms: 1.02x faster                                                       |
| go                      | 135 ms                                                                 | 133 ms: 1.02x faster                                                       |
| sympy_expand            | 459 ms                                                                 | 452 ms: 1.02x faster                                                       |
| scimark_lu              | 108 ms                                                                 | 106 ms: 1.02x faster                                                       |
| 2to3                    | 254 ms                                                                 | 251 ms: 1.02x faster                                                       |
| deepcopy                | 331 us                                                                 | 326 us: 1.02x faster                                                       |
| unpickle_list           | 5.10 us                                                                | 5.04 us: 1.01x faster                                                      |
| raytrace                | 286 ms                                                                 | 283 ms: 1.01x faster                                                       |
| meteor_contest          | 106 ms                                                                 | 105 ms: 1.01x faster                                                       |
| richards                | 42.4 ms                                                                | 41.9 ms: 1.01x faster                                                      |
| generators              | 76.9 ms                                                                | 76.0 ms: 1.01x faster                                                      |
| regex_v8                | 22.6 ms                                                                | 22.4 ms: 1.01x faster                                                      |
| sympy_str               | 272 ms                                                                 | 269 ms: 1.01x faster                                                       |
| logging_format          | 6.38 us                                                                | 6.32 us: 1.01x faster                                                      |
| regex_dna               | 219 ms                                                                 | 217 ms: 1.01x faster                                                       |
| sympy_sum               | 156 ms                                                                 | 155 ms: 1.01x faster                                                       |
| genshi_text             | 20.9 ms                                                                | 20.7 ms: 1.01x faster                                                      |
| sympy_integrate         | 19.8 ms                                                                | 19.6 ms: 1.01x faster                                                      |
| pickle_pure_python      | 285 us                                                                 | 283 us: 1.01x faster                                                       |
| regex_compile           | 129 ms                                                                 | 128 ms: 1.01x faster                                                       |
| sqlglot_parse           | 1.43 ms                                                                | 1.42 ms: 1.01x faster                                                      |
| pyflate                 | 404 ms                                                                 | 402 ms: 1.01x faster                                                       |
| gunicorn                | 1.07 ms                                                                | 1.07 ms: 1.01x faster                                                      |
| docutils                | 2.51 sec                                                               | 2.50 sec: 1.00x faster                                                     |
| bench_thread_pool       | 782 us                                                                 | 785 us: 1.00x slower                                                       |
| aiohttp                 | 998 us                                                                 | 1.00 ms: 1.00x slower                                                      |
| genshi_xml              | 46.6 ms                                                                | 46.8 ms: 1.00x slower                                                      |
| thrift                  | 746 us                                                                 | 750 us: 1.01x slower                                                       |
| json_loads              | 24.1 us                                                                | 24.3 us: 1.01x slower                                                      |
| async_generators        | 351 ms                                                                 | 353 ms: 1.01x slower                                                       |
| create_gc_cycles        | 1.46 ms                                                                | 1.47 ms: 1.01x slower                                                      |
| async_tree_io           | 1.32 sec                                                               | 1.33 sec: 1.01x slower                                                     |
| xml_etree_parse         | 147 ms                                                                 | 148 ms: 1.01x slower                                                       |
| xml_etree_generate      | 77.3 ms                                                                | 78.0 ms: 1.01x slower                                                      |
| pickle                  | 10.2 us                                                                | 10.3 us: 1.01x slower                                                      |
| coroutines              | 25.9 ms                                                                | 26.2 ms: 1.01x slower                                                      |
| unpack_sequence         | 42.1 ns                                                                | 42.6 ns: 1.01x slower                                                      |
| async_tree_cpu_io_mixed | 750 ms                                                                 | 758 ms: 1.01x slower                                                       |
| pathlib                 | 17.7 ms                                                                | 18.0 ms: 1.01x slower                                                      |
| spectral_norm           | 95.7 ms                                                                | 96.9 ms: 1.01x slower                                                      |
| json                    | 4.62 ms                                                                | 4.69 ms: 1.01x slower                                                      |
| unpickle_pure_python    | 197 us                                                                 | 200 us: 1.02x slower                                                       |
| chaos                   | 63.8 ms                                                                | 64.8 ms: 1.02x slower                                                      |
| telco                   | 6.44 ms                                                                | 6.55 ms: 1.02x slower                                                      |
| django_template         | 32.5 ms                                                                | 33.0 ms: 1.02x slower                                                      |
| float                   | 72.7 ms                                                                | 74.2 ms: 1.02x slower                                                      |
| crypto_pyaes            | 72.6 ms                                                                | 74.2 ms: 1.02x slower                                                      |
| nqueens                 | 75.0 ms                                                                | 76.9 ms: 1.02x slower                                                      |
| mako                    | 9.53 ms                                                                | 9.85 ms: 1.03x slower                                                      |
| regex_effbot            | 3.61 ms                                                                | 3.76 ms: 1.04x slower                                                      |
| pidigits                | 189 ms                                                                 | 198 ms: 1.04x slower                                                       |
| gc_traversal            | 3.65 ms                                                                | 3.82 ms: 1.05x slower                                                      |
| coverage                | 95.2 ms                                                                | 100 ms: 1.05x slower                                                       |
| pickle_list             | 3.98 us                                                                | 4.25 us: 1.07x slower                                                      |
| pickle_dict             | 29.9 us                                                                | 32.4 us: 1.08x slower                                                      |
| Geometric mean          | (ref)                                                                  | 1.00x slower                                                               |

Benchmark hidden because not significant (32): html5lib, unpickle, djangocms, sqlglot_transpile, nbody, tornado_http, xml_etree_process, scimark_fft, dask, async_tree_memoization, sqlglot_normalize, chameleon, sqlglot_optimize, bench_mp_pool, pprint_safe_repr, scimark_sparse_mat_mult, mypy, async_tree_none, scimark_monte_carlo, logging_simple, mdp, pprint_pformat, dulwich_log, hexiom, asyncio_tcp, deepcopy_memo, xml_etree_iterparse, pycparser, sqlite_synth, json_dumps, deepcopy_reduce, scimark_sor
