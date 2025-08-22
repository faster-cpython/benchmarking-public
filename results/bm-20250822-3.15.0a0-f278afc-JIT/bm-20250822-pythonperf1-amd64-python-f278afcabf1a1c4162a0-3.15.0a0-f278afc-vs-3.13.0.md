# Results vs. 3.13.0

- fork: python
- ref: f278afcabf1a1c4162a0
- machine: windows-amd64
- commit hash: f278afc
- commit date: 2025-08-22
- overall geometric mean: 1.107x faster
- HPT reliability: 99.95%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250822-pythonperf1-amd64-python-f278afcabf1a1c4162a0-3.15.0a0-f278afc |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| docutils       | 1.53 sec                                                    | 1.61 sec: 1.05x slower                                                     |
| Geometric mean | (ref)                                                       | 1.01x slower                                                               |

Benchmark hidden because not significant (3): 2to3, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250822-pythonperf1-amd64-python-f278afcabf1a1c4162a0-3.15.0a0-f278afc |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 158 ms: 1.90x faster                                                       |
| async_tree_io              | 513 ms                                                      | 378 ms: 1.36x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 208 ms: 1.35x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 199 ms: 1.33x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 376 ms: 1.32x faster                                                       |
| async_tree_none            | 219 ms                                                      | 172 ms: 1.27x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 165 ms: 1.21x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 328 ms: 1.16x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 332 ms: 1.15x faster                                                       |
| async_generators           | 223 ms                                                      | 241 ms: 1.08x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 14.4 ms: 1.15x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.23x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250822-pythonperf1-amd64-python-f278afcabf1a1c4162a0-3.15.0a0-f278afc |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 66.3 ms                                                     | 53.6 ms: 1.24x faster                                                      |
| float          | 50.8 ms                                                     | 42.6 ms: 1.19x faster                                                      |
| pidigits       | 146 ms                                                      | 144 ms: 1.02x faster                                                       |
| Geometric mean | (ref)                                                       | 1.14x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250822-pythonperf1-amd64-python-f278afcabf1a1c4162a0-3.15.0a0-f278afc |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 13.7 ms: 1.74x faster                                                      |
| regex_effbot   | 1.69 ms                                                     | 1.56 ms: 1.08x faster                                                      |
| regex_compile  | 80.7 ms                                                     | 77.0 ms: 1.05x faster                                                      |
| regex_dna      | 115 ms                                                      | 118 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                       | 1.18x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250822-pythonperf1-amd64-python-f278afcabf1a1c4162a0-3.15.0a0-f278afc |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads          | 1.37 sec                                                    | 1.08 sec: 1.27x faster                                                     |
| unpickle_pure_python | 130 us                                                      | 104 us: 1.25x faster                                                       |
| json_dumps           | 6.19 ms                                                     | 5.42 ms: 1.14x faster                                                      |
| xml_etree_parse      | 92.2 ms                                                     | 84.2 ms: 1.09x faster                                                      |
| xml_etree_generate   | 53.5 ms                                                     | 49.2 ms: 1.09x faster                                                      |
| json_loads           | 15.1 us                                                     | 14.2 us: 1.06x faster                                                      |
| xml_etree_process    | 36.5 ms                                                     | 34.6 ms: 1.06x faster                                                      |
| pickle_pure_python   | 186 us                                                      | 198 us: 1.07x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.09x faster                                                               |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250822-pythonperf1-amd64-python-f278afcabf1a1c4162a0-3.15.0a0-f278afc |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 25.3 ms: 1.04x slower                                                      |
| python_startup_no_site | 16.9 ms                                                     | 19.0 ms: 1.12x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.08x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250822-pythonperf1-amd64-python-f278afcabf1a1c4162a0-3.15.0a0-f278afc |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 6.56 ms                                                     | 5.36 ms: 1.22x faster                                                      |
| genshi_text     | 15.2 ms                                                     | 15.5 ms: 1.02x slower                                                      |
| django_template | 20.3 ms                                                     | 23.8 ms: 1.17x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.00x faster                                                               |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250822-pythonperf1-amd64-python-f278afcabf1a1c4162a0-3.15.0a0-f278afc |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 486 us: 17.41x faster                                                      |
| pathlib                    | 75.3 ms                                                     | 29.6 ms: 2.54x faster                                                      |
| asyncio_websockets         | 300 ms                                                      | 158 ms: 1.90x faster                                                       |
| mdp                        | 1.43 sec                                                    | 775 ms: 1.85x faster                                                       |
| regex_v8                   | 23.8 ms                                                     | 13.7 ms: 1.74x faster                                                      |
| async_tree_io              | 513 ms                                                      | 378 ms: 1.36x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 208 ms: 1.35x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 199 ms: 1.33x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 376 ms: 1.32x faster                                                       |
| deepcopy                   | 223 us                                                      | 172 us: 1.30x faster                                                       |
| telco                      | 4.85 ms                                                     | 3.79 ms: 1.28x faster                                                      |
| async_tree_none            | 219 ms                                                      | 172 ms: 1.27x faster                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.08 sec: 1.27x faster                                                     |
| unpickle_pure_python       | 130 us                                                      | 104 us: 1.25x faster                                                       |
| nbody                      | 66.3 ms                                                     | 53.6 ms: 1.24x faster                                                      |
| fannkuch                   | 252 ms                                                      | 204 ms: 1.23x faster                                                       |
| mako                       | 6.56 ms                                                     | 5.36 ms: 1.22x faster                                                      |
| async_tree_none_tg         | 200 ms                                                      | 165 ms: 1.21x faster                                                       |
| deepcopy_memo              | 23.1 us                                                     | 19.0 us: 1.21x faster                                                      |
| float                      | 50.8 ms                                                     | 42.6 ms: 1.19x faster                                                      |
| scimark_fft                | 175 ms                                                      | 150 ms: 1.17x faster                                                       |
| bpe_tokeniser              | 2.87 sec                                                    | 2.48 sec: 1.16x faster                                                     |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 328 ms: 1.16x faster                                                       |
| pprint_safe_repr           | 485 ms                                                      | 419 ms: 1.16x faster                                                       |
| pprint_pformat             | 977 ms                                                      | 847 ms: 1.15x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 332 ms: 1.15x faster                                                       |
| json_dumps                 | 6.19 ms                                                     | 5.42 ms: 1.14x faster                                                      |
| go                         | 84.7 ms                                                     | 74.8 ms: 1.13x faster                                                      |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.31 ms: 1.13x faster                                                      |
| xml_etree_parse            | 92.2 ms                                                     | 84.2 ms: 1.09x faster                                                      |
| deepcopy_reduce            | 2.02 us                                                     | 1.85 us: 1.09x faster                                                      |
| json                       | 3.30 ms                                                     | 3.03 ms: 1.09x faster                                                      |
| xml_etree_generate         | 53.5 ms                                                     | 49.2 ms: 1.09x faster                                                      |
| regex_effbot               | 1.69 ms                                                     | 1.56 ms: 1.08x faster                                                      |
| pyflate                    | 283 ms                                                      | 263 ms: 1.08x faster                                                       |
| k_core                     | 1.70 sec                                                    | 1.59 sec: 1.07x faster                                                     |
| pylint                     | 205 ms                                                      | 194 ms: 1.06x faster                                                       |
| json_loads                 | 15.1 us                                                     | 14.2 us: 1.06x faster                                                      |
| xml_etree_process          | 36.5 ms                                                     | 34.6 ms: 1.06x faster                                                      |
| regex_compile              | 80.7 ms                                                     | 77.0 ms: 1.05x faster                                                      |
| typing_runtime_protocols   | 103 us                                                      | 98.7 us: 1.04x faster                                                      |
| meteor_contest             | 72.0 ms                                                     | 69.3 ms: 1.04x faster                                                      |
| sqlite_synth               | 1.59 us                                                     | 1.53 us: 1.03x faster                                                      |
| dulwich_log                | 40.1 ms                                                     | 39.0 ms: 1.03x faster                                                      |
| scimark_monte_carlo        | 40.7 ms                                                     | 39.7 ms: 1.03x faster                                                      |
| crypto_pyaes               | 45.6 ms                                                     | 44.7 ms: 1.02x faster                                                      |
| logging_silent             | 54.6 ns                                                     | 53.7 ns: 1.02x faster                                                      |
| shortest_path              | 355 ms                                                      | 350 ms: 1.02x faster                                                       |
| connected_components       | 320 ms                                                      | 315 ms: 1.02x faster                                                       |
| pidigits                   | 146 ms                                                      | 144 ms: 1.02x faster                                                       |
| scimark_sor                | 76.2 ms                                                     | 75.5 ms: 1.01x faster                                                      |
| spectral_norm              | 63.4 ms                                                     | 62.9 ms: 1.01x faster                                                      |
| sympy_expand               | 286 ms                                                      | 289 ms: 1.01x slower                                                       |
| richards                   | 26.3 ms                                                     | 26.6 ms: 1.01x slower                                                      |
| richards_super             | 29.8 ms                                                     | 30.3 ms: 1.02x slower                                                      |
| genshi_text                | 15.2 ms                                                     | 15.5 ms: 1.02x slower                                                      |
| logging_simple             | 5.77 us                                                     | 5.92 us: 1.02x slower                                                      |
| hexiom                     | 3.84 ms                                                     | 3.94 ms: 1.02x slower                                                      |
| scimark_lu                 | 56.7 ms                                                     | 58.1 ms: 1.02x slower                                                      |
| regex_dna                  | 115 ms                                                      | 118 ms: 1.03x slower                                                       |
| python_startup             | 24.4 ms                                                     | 25.3 ms: 1.04x slower                                                      |
| logging_format             | 6.18 us                                                     | 6.41 us: 1.04x slower                                                      |
| nqueens                    | 56.1 ms                                                     | 58.8 ms: 1.05x slower                                                      |
| docutils                   | 1.53 sec                                                    | 1.61 sec: 1.05x slower                                                     |
| chaos                      | 37.9 ms                                                     | 39.9 ms: 1.05x slower                                                      |
| gc_traversal               | 1.96 ms                                                     | 2.08 ms: 1.06x slower                                                      |
| create_gc_cycles           | 1.22 ms                                                     | 1.30 ms: 1.06x slower                                                      |
| pickle_pure_python         | 186 us                                                      | 198 us: 1.07x slower                                                       |
| coverage                   | 45.3 ms                                                     | 48.9 ms: 1.08x slower                                                      |
| async_generators           | 223 ms                                                      | 241 ms: 1.08x slower                                                       |
| raytrace                   | 153 ms                                                      | 168 ms: 1.09x slower                                                       |
| python_startup_no_site     | 16.9 ms                                                     | 19.0 ms: 1.12x slower                                                      |
| coroutines                 | 12.5 ms                                                     | 14.4 ms: 1.15x slower                                                      |
| deltablue                  | 1.89 ms                                                     | 2.18 ms: 1.15x slower                                                      |
| django_template            | 20.3 ms                                                     | 23.8 ms: 1.17x slower                                                      |
| many_optionals             | 361 us                                                      | 561 us: 1.55x slower                                                       |
| subparsers                 | 10.9 ms                                                     | 29.8 ms: 2.75x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.10x faster                                                               |

Benchmark hidden because not significant (11): pycparser, 2to3, comprehensions, sympy_str, sympy_integrate, generators, sympy_sum, sphinx, genshi_xml, html5lib, xml_etree_iterparse
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250822-3.15.0a0-f278afc-JIT/bm-20250822-pythonperf1-amd64-python-f278afcabf1a1c4162a0-3.15.0a0-f278afc.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.107x faster

# HPT report

- Reliability score: 99.95% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown