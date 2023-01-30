
# Results vs. base

- fork: iritkatriel
- ref: stdlib_single_arg_ex
- machine: linux-x86_64
- commit hash: 23ae36b
- commit date: 2023-01-29
- overall geometric mean: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230126-linux-x86_64-python-409f5337a3e466a5ef67-3.12.0a4+-409f533 | bm-20230129-linux-x86_64-iritkatriel-stdlib_single_arg_ex-3.12.0a4+-23ae36b |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 250 ms                                                                 | 251 ms: 1.00x slower                                                        |
| chameleon      | 6.29 ms                                                                | 6.36 ms: 1.01x slower                                                       |
| docutils       | 2.50 sec                                                               | 2.48 sec: 1.01x faster                                                      |
| tornado_http   | 94.4 ms                                                                | 93.8 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                                |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230126-linux-x86_64-python-409f5337a3e466a5ef67-3.12.0a4+-409f533 | bm-20230129-linux-x86_64-iritkatriel-stdlib_single_arg_ex-3.12.0a4+-23ae36b |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 193 ms                                                                 | 193 ms: 1.00x slower                                                        |
| float          | 71.9 ms                                                                | 73.8 ms: 1.03x slower                                                       |
| nbody          | 92.9 ms                                                                | 95.6 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                                  | 1.02x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230126-linux-x86_64-python-409f5337a3e466a5ef67-3.12.0a4+-409f533 | bm-20230129-linux-x86_64-iritkatriel-stdlib_single_arg_ex-3.12.0a4+-23ae36b |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 128 ms                                                                 | 128 ms: 1.01x faster                                                        |
| regex_v8       | 21.1 ms                                                                | 21.0 ms: 1.00x faster                                                       |
| regex_dna      | 201 ms                                                                 | 202 ms: 1.00x slower                                                        |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                                |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230126-linux-x86_64-python-409f5337a3e466a5ef67-3.12.0a4+-409f533 | bm-20230129-linux-x86_64-iritkatriel-stdlib_single_arg_ex-3.12.0a4+-23ae36b |
|----------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_iterparse  | 107 ms                                                                 | 102 ms: 1.04x faster                                                        |
| unpickle             | 13.2 us                                                                | 13.0 us: 1.02x faster                                                       |
| unpickle_list        | 5.00 us                                                                | 4.94 us: 1.01x faster                                                       |
| xml_etree_process    | 53.5 ms                                                                | 53.2 ms: 1.01x faster                                                       |
| json_dumps           | 9.31 ms                                                                | 9.36 ms: 1.01x slower                                                       |
| unpickle_pure_python | 198 us                                                                 | 199 us: 1.01x slower                                                        |
| Geometric mean       | (ref)                                                                  | 1.01x faster                                                                |

Benchmark hidden because not significant (7): xml_etree_parse, pickle_pure_python, json_loads, pickle_dict, pickle_list, pickle, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230126-linux-x86_64-python-409f5337a3e466a5ef67-3.12.0a4+-409f533 | bm-20230129-linux-x86_64-iritkatriel-stdlib_single_arg_ex-3.12.0a4+-23ae36b |
|------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 8.95 ms                                                                | 8.93 ms: 1.00x faster                                                       |
| python_startup_no_site | 6.47 ms                                                                | 6.46 ms: 1.00x faster                                                       |
| Geometric mean         | (ref)                                                                  | 1.00x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20230126-linux-x86_64-python-409f5337a3e466a5ef67-3.12.0a4+-409f533 | bm-20230129-linux-x86_64-iritkatriel-stdlib_single_arg_ex-3.12.0a4+-23ae36b |
|-----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 20.6 ms                                                                | 20.3 ms: 1.02x faster                                                       |
| django_template | 32.8 ms                                                                | 32.3 ms: 1.01x faster                                                       |
| mako            | 9.70 ms                                                                | 9.85 ms: 1.02x slower                                                       |
| genshi_xml      | 46.4 ms                                                                | 47.5 ms: 1.02x slower                                                       |
| Geometric mean  | (ref)                                                                  | 1.00x slower                                                                |

All benchmarks:
===============

| Benchmark               | bm-20230126-linux-x86_64-python-409f5337a3e466a5ef67-3.12.0a4+-409f533 | bm-20230129-linux-x86_64-iritkatriel-stdlib_single_arg_ex-3.12.0a4+-23ae36b |
|-------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpack_sequence         | 44.3 ns                                                                | 42.5 ns: 1.04x faster                                                       |
| xml_etree_iterparse     | 107 ms                                                                 | 102 ms: 1.04x faster                                                        |
| spectral_norm           | 97.0 ms                                                                | 94.4 ms: 1.03x faster                                                       |
| meteor_contest          | 106 ms                                                                 | 104 ms: 1.02x faster                                                        |
| chaos                   | 65.8 ms                                                                | 64.5 ms: 1.02x faster                                                       |
| fannkuch                | 365 ms                                                                 | 358 ms: 1.02x faster                                                        |
| hexiom                  | 5.97 ms                                                                | 5.86 ms: 1.02x faster                                                       |
| coroutines              | 25.4 ms                                                                | 24.9 ms: 1.02x faster                                                       |
| bench_thread_pool       | 775 us                                                                 | 761 us: 1.02x faster                                                        |
| pprint_pformat          | 1.39 sec                                                               | 1.36 sec: 1.02x faster                                                      |
| unpickle                | 13.2 us                                                                | 13.0 us: 1.02x faster                                                       |
| genshi_text             | 20.6 ms                                                                | 20.3 ms: 1.02x faster                                                       |
| django_template         | 32.8 ms                                                                | 32.3 ms: 1.01x faster                                                       |
| logging_silent          | 91.3 ns                                                                | 90.0 ns: 1.01x faster                                                       |
| async_tree_io           | 1.32 sec                                                               | 1.31 sec: 1.01x faster                                                      |
| sympy_expand            | 456 ms                                                                 | 451 ms: 1.01x faster                                                        |
| unpickle_list           | 5.00 us                                                                | 4.94 us: 1.01x faster                                                       |
| deepcopy_memo           | 34.4 us                                                                | 34.1 us: 1.01x faster                                                       |
| dask                    | 498 ms                                                                 | 492 ms: 1.01x faster                                                        |
| sqlglot_transpile       | 1.70 ms                                                                | 1.69 ms: 1.01x faster                                                       |
| raytrace                | 282 ms                                                                 | 280 ms: 1.01x faster                                                        |
| pprint_safe_repr        | 676 ms                                                                 | 670 ms: 1.01x faster                                                        |
| docutils                | 2.50 sec                                                               | 2.48 sec: 1.01x faster                                                      |
| asyncio_tcp             | 499 ms                                                                 | 495 ms: 1.01x faster                                                        |
| dulwich_log             | 62.6 ms                                                                | 62.1 ms: 1.01x faster                                                       |
| async_tree_cpu_io_mixed | 760 ms                                                                 | 755 ms: 1.01x faster                                                        |
| deepcopy_reduce         | 2.97 us                                                                | 2.95 us: 1.01x faster                                                       |
| tornado_http            | 94.4 ms                                                                | 93.8 ms: 1.01x faster                                                       |
| deepcopy                | 329 us                                                                 | 327 us: 1.01x faster                                                        |
| regex_compile           | 128 ms                                                                 | 128 ms: 1.01x faster                                                        |
| sqlglot_parse           | 1.41 ms                                                                | 1.40 ms: 1.01x faster                                                       |
| logging_format          | 6.35 us                                                                | 6.31 us: 1.01x faster                                                       |
| create_gc_cycles        | 1.48 ms                                                                | 1.47 ms: 1.01x faster                                                       |
| xml_etree_process       | 53.5 ms                                                                | 53.2 ms: 1.01x faster                                                       |
| regex_v8                | 21.1 ms                                                                | 21.0 ms: 1.00x faster                                                       |
| python_startup          | 8.95 ms                                                                | 8.93 ms: 1.00x faster                                                       |
| python_startup_no_site  | 6.47 ms                                                                | 6.46 ms: 1.00x faster                                                       |
| pidigits                | 193 ms                                                                 | 193 ms: 1.00x slower                                                        |
| mdp                     | 2.57 sec                                                               | 2.57 sec: 1.00x slower                                                      |
| sympy_integrate         | 19.7 ms                                                                | 19.7 ms: 1.00x slower                                                       |
| regex_dna               | 201 ms                                                                 | 202 ms: 1.00x slower                                                        |
| 2to3                    | 250 ms                                                                 | 251 ms: 1.00x slower                                                        |
| json_dumps              | 9.31 ms                                                                | 9.36 ms: 1.01x slower                                                       |
| unpickle_pure_python    | 198 us                                                                 | 199 us: 1.01x slower                                                        |
| generators              | 76.4 ms                                                                | 76.9 ms: 1.01x slower                                                       |
| scimark_sor             | 105 ms                                                                 | 106 ms: 1.01x slower                                                        |
| scimark_sparse_mat_mult | 4.03 ms                                                                | 4.06 ms: 1.01x slower                                                       |
| sqlglot_normalize       | 104 ms                                                                 | 105 ms: 1.01x slower                                                        |
| scimark_monte_carlo     | 65.5 ms                                                                | 66.1 ms: 1.01x slower                                                       |
| go                      | 132 ms                                                                 | 133 ms: 1.01x slower                                                        |
| chameleon               | 6.29 ms                                                                | 6.36 ms: 1.01x slower                                                       |
| pathlib                 | 17.8 ms                                                                | 18.0 ms: 1.01x slower                                                       |
| mako                    | 9.70 ms                                                                | 9.85 ms: 1.02x slower                                                       |
| telco                   | 6.28 ms                                                                | 6.38 ms: 1.02x slower                                                       |
| sqlite_synth            | 2.58 us                                                                | 2.62 us: 1.02x slower                                                       |
| genshi_xml              | 46.4 ms                                                                | 47.5 ms: 1.02x slower                                                       |
| pyflate                 | 396 ms                                                                 | 406 ms: 1.02x slower                                                        |
| scimark_fft             | 298 ms                                                                 | 305 ms: 1.03x slower                                                        |
| float                   | 71.9 ms                                                                | 73.8 ms: 1.03x slower                                                       |
| nbody                   | 92.9 ms                                                                | 95.6 ms: 1.03x slower                                                       |
| nqueens                 | 76.3 ms                                                                | 79.1 ms: 1.04x slower                                                       |
| gc_traversal            | 3.81 ms                                                                | 4.29 ms: 1.12x slower                                                       |
| Geometric mean          | (ref)                                                                  | 1.00x faster                                                                |

Benchmark hidden because not significant (29): html5lib, async_tree_none, json, coverage, sympy_str, djangocms, crypto_pyaes, xml_etree_parse, mypy, pickle_pure_python, thrift, json_loads, richards, pycparser, sqlglot_optimize, pickle_dict, deltablue, bench_mp_pool, pickle_list, pickle, sympy_sum, async_generators, aiohttp, regex_effbot, logging_simple, xml_etree_generate, gunicorn, scimark_lu, async_tree_memoization
