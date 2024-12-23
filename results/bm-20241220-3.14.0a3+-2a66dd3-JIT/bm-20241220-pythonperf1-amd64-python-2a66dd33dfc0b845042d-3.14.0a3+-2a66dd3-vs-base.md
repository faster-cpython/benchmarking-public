# Results vs. base

- fork: python
- ref: 2a66dd33dfc0b845042d
- machine: windows-amd64
- commit hash: 2a66dd3
- commit date: 2024-12-20
- overall geometric mean: 1.046x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20241220-3.14.0a3+-2a66dd3/bm-20241220-pythonperf1-amd64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3.json | results/bm-20241220-3.14.0a3+-2a66dd3-JIT/bm-20241220-pythonperf1-amd64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3.json |
|----------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 226 ms                                                                                                                 | 221 ms: 1.03x faster                                                                                                       |
| docutils       | 1.68 sec                                                                                                               | 1.73 sec: 1.03x slower                                                                                                     |
| html5lib       | 40.9 ms                                                                                                                | 39.6 ms: 1.03x faster                                                                                                      |
| sphinx         | 655 ms                                                                                                                 | 675 ms: 1.03x slower                                                                                                       |
| Geometric mean | (ref)                                                                                                                  | 1.00x slower                                                                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark              | results/bm-20241220-3.14.0a3+-2a66dd3/bm-20241220-pythonperf1-amd64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3.json | results/bm-20241220-3.14.0a3+-2a66dd3-JIT/bm-20241220-pythonperf1-amd64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3.json |
|------------------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| async_tree_io          | 412 ms                                                                                                                 | 403 ms: 1.02x faster                                                                                                       |
| async_tree_memoization | 229 ms                                                                                                                 | 224 ms: 1.02x faster                                                                                                       |
| async_tree_io_tg       | 409 ms                                                                                                                 | 401 ms: 1.02x faster                                                                                                       |
| asyncio_websockets     | 308 ms                                                                                                                 | 303 ms: 1.01x faster                                                                                                       |
| coroutines             | 13.5 ms                                                                                                                | 13.4 ms: 1.01x faster                                                                                                      |
| async_tree_none        | 186 ms                                                                                                                 | 184 ms: 1.01x faster                                                                                                       |
| async_tree_none_tg     | 175 ms                                                                                                                 | 173 ms: 1.01x faster                                                                                                       |
| async_generators       | 235 ms                                                                                                                 | 260 ms: 1.11x slower                                                                                                       |
| Geometric mean         | (ref)                                                                                                                  | 1.00x faster                                                                                                               |

Benchmark hidden because not significant (3): async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20241220-3.14.0a3+-2a66dd3/bm-20241220-pythonperf1-amd64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3.json | results/bm-20241220-3.14.0a3+-2a66dd3-JIT/bm-20241220-pythonperf1-amd64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3.json |
|----------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| nbody          | 82.0 ms                                                                                                                | 53.0 ms: 1.55x faster                                                                                                      |
| float          | 55.3 ms                                                                                                                | 45.9 ms: 1.20x faster                                                                                                      |
| pidigits       | 147 ms                                                                                                                 | 147 ms: 1.01x faster                                                                                                       |
| Geometric mean | (ref)                                                                                                                  | 1.23x faster                                                                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20241220-3.14.0a3+-2a66dd3/bm-20241220-pythonperf1-amd64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3.json | results/bm-20241220-3.14.0a3+-2a66dd3-JIT/bm-20241220-pythonperf1-amd64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3.json |
|----------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| regex_compile  | 88.7 ms                                                                                                                | 80.4 ms: 1.10x faster                                                                                                      |
| regex_dna      | 117 ms                                                                                                                 | 113 ms: 1.03x faster                                                                                                       |
| regex_effbot   | 1.45 ms                                                                                                                | 1.42 ms: 1.02x faster                                                                                                      |
| Geometric mean | (ref)                                                                                                                  | 1.05x faster                                                                                                               |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20241220-3.14.0a3+-2a66dd3/bm-20241220-pythonperf1-amd64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3.json | results/bm-20241220-3.14.0a3+-2a66dd3-JIT/bm-20241220-pythonperf1-amd64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3.json |
|----------------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| unpickle_pure_python | 151 us                                                                                                                 | 110 us: 1.37x faster                                                                                                       |
| tomli_loads          | 1.46 sec                                                                                                               | 1.20 sec: 1.22x faster                                                                                                     |
| xml_etree_generate   | 58.3 ms                                                                                                                | 50.5 ms: 1.15x faster                                                                                                      |
| xml_etree_process    | 40.4 ms                                                                                                                | 35.9 ms: 1.13x faster                                                                                                      |
| pickle_pure_python   | 228 us                                                                                                                 | 212 us: 1.07x faster                                                                                                       |
| xml_etree_iterparse  | 63.1 ms                                                                                                                | 58.8 ms: 1.07x faster                                                                                                      |
| json_dumps           | 6.74 ms                                                                                                                | 6.41 ms: 1.05x faster                                                                                                      |
| xml_etree_parse      | 88.3 ms                                                                                                                | 85.9 ms: 1.03x faster                                                                                                      |
| Geometric mean       | (ref)                                                                                                                  | 1.12x faster                                                                                                               |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20241220-3.14.0a3+-2a66dd3/bm-20241220-pythonperf1-amd64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3.json | results/bm-20241220-3.14.0a3+-2a66dd3-JIT/bm-20241220-pythonperf1-amd64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3.json |
|-----------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| mako            | 6.78 ms                                                                                                                | 5.13 ms: 1.32x faster                                                                                                      |
| django_template | 25.6 ms                                                                                                                | 27.1 ms: 1.06x slower                                                                                                      |
| genshi_text     | 16.7 ms                                                                                                                | 18.7 ms: 1.11x slower                                                                                                      |
| genshi_xml      | 35.0 ms                                                                                                                | 46.2 ms: 1.32x slower                                                                                                      |
| Geometric mean  | (ref)                                                                                                                  | 1.04x slower                                                                                                               |

All benchmarks:
===============

| Benchmark                | results/bm-20241220-3.14.0a3+-2a66dd3/bm-20241220-pythonperf1-amd64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3.json | results/bm-20241220-3.14.0a3+-2a66dd3-JIT/bm-20241220-pythonperf1-amd64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3.json |
|--------------------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| nbody                    | 82.0 ms                                                                                                                | 53.0 ms: 1.55x faster                                                                                                      |
| scimark_sor              | 89.5 ms                                                                                                                | 63.9 ms: 1.40x faster                                                                                                      |
| unpickle_pure_python     | 151 us                                                                                                                 | 110 us: 1.37x faster                                                                                                       |
| scimark_fft              | 194 ms                                                                                                                 | 143 ms: 1.36x faster                                                                                                       |
| mako                     | 6.78 ms                                                                                                                | 5.13 ms: 1.32x faster                                                                                                      |
| scimark_sparse_mat_mult  | 2.62 ms                                                                                                                | 2.05 ms: 1.28x faster                                                                                                      |
| spectral_norm            | 62.9 ms                                                                                                                | 49.4 ms: 1.27x faster                                                                                                      |
| scimark_monte_carlo      | 47.6 ms                                                                                                                | 37.4 ms: 1.27x faster                                                                                                      |
| deepcopy_memo            | 20.8 us                                                                                                                | 16.8 us: 1.24x faster                                                                                                      |
| tomli_loads              | 1.46 sec                                                                                                               | 1.20 sec: 1.22x faster                                                                                                     |
| float                    | 55.3 ms                                                                                                                | 45.9 ms: 1.20x faster                                                                                                      |
| crypto_pyaes             | 47.9 ms                                                                                                                | 40.8 ms: 1.17x faster                                                                                                      |
| xml_etree_generate       | 58.3 ms                                                                                                                | 50.5 ms: 1.15x faster                                                                                                      |
| fannkuch                 | 282 ms                                                                                                                 | 246 ms: 1.15x faster                                                                                                       |
| scimark_lu               | 62.6 ms                                                                                                                | 54.7 ms: 1.15x faster                                                                                                      |
| telco                    | 4.86 ms                                                                                                                | 4.27 ms: 1.14x faster                                                                                                      |
| bpe_tokeniser            | 3.00 sec                                                                                                               | 2.64 sec: 1.14x faster                                                                                                     |
| xml_etree_process        | 40.4 ms                                                                                                                | 35.9 ms: 1.13x faster                                                                                                      |
| pprint_safe_repr         | 558 ms                                                                                                                 | 497 ms: 1.12x faster                                                                                                       |
| pprint_pformat           | 1.11 sec                                                                                                               | 996 ms: 1.12x faster                                                                                                       |
| logging_silent           | 62.3 ns                                                                                                                | 56.3 ns: 1.11x faster                                                                                                      |
| regex_compile            | 88.7 ms                                                                                                                | 80.4 ms: 1.10x faster                                                                                                      |
| pyflate                  | 316 ms                                                                                                                 | 288 ms: 1.10x faster                                                                                                       |
| pickle_pure_python       | 228 us                                                                                                                 | 212 us: 1.07x faster                                                                                                       |
| xml_etree_iterparse      | 63.1 ms                                                                                                                | 58.8 ms: 1.07x faster                                                                                                      |
| pycparser                | 764 ms                                                                                                                 | 714 ms: 1.07x faster                                                                                                       |
| sqlglot_parse            | 903 us                                                                                                                 | 844 us: 1.07x faster                                                                                                       |
| k_core                   | 1.70 sec                                                                                                               | 1.60 sec: 1.07x faster                                                                                                     |
| chaos                    | 43.6 ms                                                                                                                | 41.3 ms: 1.05x faster                                                                                                      |
| json_dumps               | 6.74 ms                                                                                                                | 6.41 ms: 1.05x faster                                                                                                      |
| meteor_contest           | 77.8 ms                                                                                                                | 74.1 ms: 1.05x faster                                                                                                      |
| json                     | 3.00 ms                                                                                                                | 2.87 ms: 1.05x faster                                                                                                      |
| comprehensions           | 12.4 us                                                                                                                | 11.9 us: 1.04x faster                                                                                                      |
| connected_components     | 321 ms                                                                                                                 | 311 ms: 1.03x faster                                                                                                       |
| html5lib                 | 40.9 ms                                                                                                                | 39.6 ms: 1.03x faster                                                                                                      |
| regex_dna                | 117 ms                                                                                                                 | 113 ms: 1.03x faster                                                                                                       |
| xml_etree_parse          | 88.3 ms                                                                                                                | 85.9 ms: 1.03x faster                                                                                                      |
| dulwich_log              | 42.1 ms                                                                                                                | 41.0 ms: 1.03x faster                                                                                                      |
| thrift                   | 525 us                                                                                                                 | 512 us: 1.03x faster                                                                                                       |
| deepcopy_reduce          | 1.91 us                                                                                                                | 1.86 us: 1.03x faster                                                                                                      |
| 2to3                     | 226 ms                                                                                                                 | 221 ms: 1.03x faster                                                                                                       |
| sqlglot_transpile        | 1.12 ms                                                                                                                | 1.09 ms: 1.02x faster                                                                                                      |
| async_tree_io            | 412 ms                                                                                                                 | 403 ms: 1.02x faster                                                                                                       |
| async_tree_memoization   | 229 ms                                                                                                                 | 224 ms: 1.02x faster                                                                                                       |
| subparsers               | 16.3 ms                                                                                                                | 16.0 ms: 1.02x faster                                                                                                      |
| async_tree_io_tg         | 409 ms                                                                                                                 | 401 ms: 1.02x faster                                                                                                       |
| regex_effbot             | 1.45 ms                                                                                                                | 1.42 ms: 1.02x faster                                                                                                      |
| sqlite_synth             | 1.60 us                                                                                                                | 1.57 us: 1.02x faster                                                                                                      |
| asyncio_websockets       | 308 ms                                                                                                                 | 303 ms: 1.01x faster                                                                                                       |
| shortest_path            | 351 ms                                                                                                                 | 346 ms: 1.01x faster                                                                                                       |
| mdp                      | 1.52 sec                                                                                                               | 1.50 sec: 1.01x faster                                                                                                     |
| coroutines               | 13.5 ms                                                                                                                | 13.4 ms: 1.01x faster                                                                                                      |
| async_tree_none          | 186 ms                                                                                                                 | 184 ms: 1.01x faster                                                                                                       |
| async_tree_none_tg       | 175 ms                                                                                                                 | 173 ms: 1.01x faster                                                                                                       |
| sympy_str                | 178 ms                                                                                                                 | 177 ms: 1.01x faster                                                                                                       |
| sympy_expand             | 305 ms                                                                                                                 | 303 ms: 1.01x faster                                                                                                       |
| pidigits                 | 147 ms                                                                                                                 | 147 ms: 1.01x faster                                                                                                       |
| typing_runtime_protocols | 113 us                                                                                                                 | 114 us: 1.01x slower                                                                                                       |
| sympy_sum                | 90.2 ms                                                                                                                | 91.1 ms: 1.01x slower                                                                                                      |
| logging_format           | 6.81 us                                                                                                                | 6.88 us: 1.01x slower                                                                                                      |
| coverage                 | 46.6 ms                                                                                                                | 47.1 ms: 1.01x slower                                                                                                      |
| go                       | 88.3 ms                                                                                                                | 89.9 ms: 1.02x slower                                                                                                      |
| deepcopy                 | 187 us                                                                                                                 | 191 us: 1.02x slower                                                                                                       |
| pathlib                  | 75.5 ms                                                                                                                | 77.4 ms: 1.03x slower                                                                                                      |
| sqlglot_normalize        | 200 ms                                                                                                                 | 206 ms: 1.03x slower                                                                                                       |
| many_optionals           | 445 us                                                                                                                 | 457 us: 1.03x slower                                                                                                       |
| docutils                 | 1.68 sec                                                                                                               | 1.73 sec: 1.03x slower                                                                                                     |
| sphinx                   | 655 ms                                                                                                                 | 675 ms: 1.03x slower                                                                                                       |
| sqlglot_optimize         | 36.4 ms                                                                                                                | 37.8 ms: 1.04x slower                                                                                                      |
| pylint                   | 201 ms                                                                                                                 | 209 ms: 1.04x slower                                                                                                       |
| django_template          | 25.6 ms                                                                                                                | 27.1 ms: 1.06x slower                                                                                                      |
| richards_super           | 35.6 ms                                                                                                                | 38.4 ms: 1.08x slower                                                                                                      |
| richards                 | 31.2 ms                                                                                                                | 33.7 ms: 1.08x slower                                                                                                      |
| raytrace                 | 196 ms                                                                                                                 | 212 ms: 1.08x slower                                                                                                       |
| async_generators         | 235 ms                                                                                                                 | 260 ms: 1.11x slower                                                                                                       |
| hexiom                   | 4.55 ms                                                                                                                | 5.06 ms: 1.11x slower                                                                                                      |
| genshi_text              | 16.7 ms                                                                                                                | 18.7 ms: 1.11x slower                                                                                                      |
| generators               | 20.6 ms                                                                                                                | 23.6 ms: 1.14x slower                                                                                                      |
| genshi_xml               | 35.0 ms                                                                                                                | 46.2 ms: 1.32x slower                                                                                                      |
| Geometric mean           | (ref)                                                                                                                  | 1.05x faster                                                                                                               |

Benchmark hidden because not significant (16): regex_v8, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, python_startup, gc_traversal, json_loads, deltablue, mypy2, async_tree_cpu_io_mixed, bench_thread_pool, sympy_integrate, logging_simple, nqueens, bench_mp_pool, create_gc_cycles, python_startup_no_site

- Geometric mean (including insignificant results): 1.046x faster

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown