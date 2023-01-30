
# Results vs. base

- fork: brandtbucher
- ref: quicken_at_runtime
- machine: linux-x86_64
- commit hash: 34ba834
- commit date: 2023-01-18
- overall geometric mean: 1.01x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230130-linux-x86_64-python-ea232716d3de1675478d-3.12.0a4+-ea23271 | bm-20230118-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-34ba834 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 252 ms                                                                 | 256 ms: 1.01x slower                                                       |
| chameleon      | 6.49 ms                                                                | 6.56 ms: 1.01x slower                                                      |
| docutils       | 2.49 sec                                                               | 2.50 sec: 1.00x slower                                                     |
| html5lib       | 60.1 ms                                                                | 61.4 ms: 1.02x slower                                                      |
| tornado_http   | 93.7 ms                                                                | 94.7 ms: 1.01x slower                                                      |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230130-linux-x86_64-python-ea232716d3de1675478d-3.12.0a4+-ea23271 | bm-20230118-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-34ba834 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 95.7 ms                                                                | 92.5 ms: 1.03x faster                                                      |
| pidigits       | 197 ms                                                                 | 198 ms: 1.00x slower                                                       |
| float          | 71.9 ms                                                                | 74.3 ms: 1.03x slower                                                      |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230130-linux-x86_64-python-ea232716d3de1675478d-3.12.0a4+-ea23271 | bm-20230118-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-34ba834 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 22.4 ms                                                                | 21.1 ms: 1.06x faster                                                      |
| regex_effbot   | 3.64 ms                                                                | 3.44 ms: 1.06x faster                                                      |
| regex_dna      | 210 ms                                                                 | 201 ms: 1.05x faster                                                       |
| regex_compile  | 128 ms                                                                 | 130 ms: 1.02x slower                                                       |
| Geometric mean | (ref)                                                                  | 1.04x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230130-linux-x86_64-python-ea232716d3de1675478d-3.12.0a4+-ea23271 | bm-20230118-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-34ba834 |
|----------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_process    | 53.8 ms                                                                | 53.5 ms: 1.01x faster                                                      |
| xml_etree_iterparse  | 103 ms                                                                 | 102 ms: 1.01x faster                                                       |
| xml_etree_generate   | 77.7 ms                                                                | 77.2 ms: 1.01x faster                                                      |
| pickle               | 9.95 us                                                                | 10.0 us: 1.01x slower                                                      |
| pickle_dict          | 30.3 us                                                                | 30.6 us: 1.01x slower                                                      |
| json_loads           | 24.1 us                                                                | 24.4 us: 1.01x slower                                                      |
| json_dumps           | 9.42 ms                                                                | 9.55 ms: 1.01x slower                                                      |
| unpickle             | 13.1 us                                                                | 13.3 us: 1.01x slower                                                      |
| pickle_pure_python   | 285 us                                                                 | 290 us: 1.02x slower                                                       |
| unpickle_pure_python | 197 us                                                                 | 209 us: 1.06x slower                                                       |
| Geometric mean       | (ref)                                                                  | 1.01x slower                                                               |

Benchmark hidden because not significant (3): pickle_list, xml_etree_parse, unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230130-linux-x86_64-python-ea232716d3de1675478d-3.12.0a4+-ea23271 | bm-20230118-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-34ba834 |
|------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 6.45 ms                                                                | 6.25 ms: 1.03x faster                                                      |
| python_startup         | 8.90 ms                                                                | 8.72 ms: 1.02x faster                                                      |
| Geometric mean         | (ref)                                                                  | 1.03x faster                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20230130-linux-x86_64-python-ea232716d3de1675478d-3.12.0a4+-ea23271 | bm-20230118-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-34ba834 |
|-----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 33.4 ms                                                                | 32.7 ms: 1.02x faster                                                      |
| mako            | 9.75 ms                                                                | 9.57 ms: 1.02x faster                                                      |
| genshi_text     | 20.8 ms                                                                | 20.5 ms: 1.01x faster                                                      |
| genshi_xml      | 46.8 ms                                                                | 48.1 ms: 1.03x slower                                                      |
| Geometric mean  | (ref)                                                                  | 1.01x faster                                                               |

All benchmarks:
===============

| Benchmark               | bm-20230130-linux-x86_64-python-ea232716d3de1675478d-3.12.0a4+-ea23271 | bm-20230118-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-34ba834 |
|-------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8                | 22.4 ms                                                                | 21.1 ms: 1.06x faster                                                      |
| regex_effbot            | 3.64 ms                                                                | 3.44 ms: 1.06x faster                                                      |
| gc_traversal            | 4.03 ms                                                                | 3.81 ms: 1.06x faster                                                      |
| regex_dna               | 210 ms                                                                 | 201 ms: 1.05x faster                                                       |
| pycparser               | 1.15 sec                                                               | 1.11 sec: 1.04x faster                                                     |
| nbody                   | 95.7 ms                                                                | 92.5 ms: 1.03x faster                                                      |
| logging_silent          | 95.3 ns                                                                | 92.3 ns: 1.03x faster                                                      |
| python_startup_no_site  | 6.45 ms                                                                | 6.25 ms: 1.03x faster                                                      |
| pprint_pformat          | 1.42 sec                                                               | 1.38 sec: 1.03x faster                                                     |
| generators              | 78.1 ms                                                                | 76.3 ms: 1.02x faster                                                      |
| django_template         | 33.4 ms                                                                | 32.7 ms: 1.02x faster                                                      |
| python_startup          | 8.90 ms                                                                | 8.72 ms: 1.02x faster                                                      |
| mako                    | 9.75 ms                                                                | 9.57 ms: 1.02x faster                                                      |
| pprint_safe_repr        | 689 ms                                                                 | 677 ms: 1.02x faster                                                       |
| spectral_norm           | 96.7 ms                                                                | 95.4 ms: 1.01x faster                                                      |
| genshi_text             | 20.8 ms                                                                | 20.5 ms: 1.01x faster                                                      |
| crypto_pyaes            | 73.3 ms                                                                | 72.8 ms: 1.01x faster                                                      |
| xml_etree_process       | 53.8 ms                                                                | 53.5 ms: 1.01x faster                                                      |
| xml_etree_iterparse     | 103 ms                                                                 | 102 ms: 1.01x faster                                                       |
| xml_etree_generate      | 77.7 ms                                                                | 77.2 ms: 1.01x faster                                                      |
| raytrace                | 283 ms                                                                 | 282 ms: 1.00x faster                                                       |
| asyncio_tcp             | 493 ms                                                                 | 491 ms: 1.00x faster                                                       |
| pidigits                | 197 ms                                                                 | 198 ms: 1.00x slower                                                       |
| docutils                | 2.49 sec                                                               | 2.50 sec: 1.00x slower                                                     |
| sqlglot_normalize       | 104 ms                                                                 | 105 ms: 1.00x slower                                                       |
| gunicorn                | 1.07 ms                                                                | 1.07 ms: 1.01x slower                                                      |
| sqlglot_transpile       | 1.69 ms                                                                | 1.70 ms: 1.01x slower                                                      |
| scimark_lu              | 106 ms                                                                 | 107 ms: 1.01x slower                                                       |
| sqlglot_parse           | 1.40 ms                                                                | 1.41 ms: 1.01x slower                                                      |
| thrift                  | 736 us                                                                 | 741 us: 1.01x slower                                                       |
| pickle                  | 9.95 us                                                                | 10.0 us: 1.01x slower                                                      |
| pickle_dict             | 30.3 us                                                                | 30.6 us: 1.01x slower                                                      |
| aiohttp                 | 993 us                                                                 | 1.00 ms: 1.01x slower                                                      |
| dulwich_log             | 62.3 ms                                                                | 62.9 ms: 1.01x slower                                                      |
| json_loads              | 24.1 us                                                                | 24.4 us: 1.01x slower                                                      |
| tornado_http            | 93.7 ms                                                                | 94.7 ms: 1.01x slower                                                      |
| chameleon               | 6.49 ms                                                                | 6.56 ms: 1.01x slower                                                      |
| logging_format          | 6.35 us                                                                | 6.42 us: 1.01x slower                                                      |
| scimark_monte_carlo     | 66.7 ms                                                                | 67.6 ms: 1.01x slower                                                      |
| sympy_integrate         | 19.7 ms                                                                | 20.0 ms: 1.01x slower                                                      |
| json_dumps              | 9.42 ms                                                                | 9.55 ms: 1.01x slower                                                      |
| 2to3                    | 252 ms                                                                 | 256 ms: 1.01x slower                                                       |
| unpickle                | 13.1 us                                                                | 13.3 us: 1.01x slower                                                      |
| regex_compile           | 128 ms                                                                 | 130 ms: 1.02x slower                                                       |
| go                      | 136 ms                                                                 | 139 ms: 1.02x slower                                                       |
| bench_thread_pool       | 775 us                                                                 | 791 us: 1.02x slower                                                       |
| deepcopy_reduce         | 2.90 us                                                                | 2.96 us: 1.02x slower                                                      |
| pickle_pure_python      | 285 us                                                                 | 290 us: 1.02x slower                                                       |
| html5lib                | 60.1 ms                                                                | 61.4 ms: 1.02x slower                                                      |
| sqlite_synth            | 2.56 us                                                                | 2.61 us: 1.02x slower                                                      |
| unpack_sequence         | 42.3 ns                                                                | 43.3 ns: 1.02x slower                                                      |
| logging_simple          | 5.72 us                                                                | 5.85 us: 1.02x slower                                                      |
| nqueens                 | 76.8 ms                                                                | 78.7 ms: 1.02x slower                                                      |
| async_generators        | 350 ms                                                                 | 359 ms: 1.02x slower                                                       |
| coroutines              | 25.1 ms                                                                | 25.8 ms: 1.03x slower                                                      |
| scimark_sparse_mat_mult | 4.06 ms                                                                | 4.16 ms: 1.03x slower                                                      |
| richards                | 42.6 ms                                                                | 43.8 ms: 1.03x slower                                                      |
| genshi_xml              | 46.8 ms                                                                | 48.1 ms: 1.03x slower                                                      |
| hexiom                  | 5.95 ms                                                                | 6.12 ms: 1.03x slower                                                      |
| dask                    | 499 ms                                                                 | 514 ms: 1.03x slower                                                       |
| mdp                     | 2.52 sec                                                               | 2.60 sec: 1.03x slower                                                     |
| float                   | 71.9 ms                                                                | 74.3 ms: 1.03x slower                                                      |
| deltablue               | 3.19 ms                                                                | 3.32 ms: 1.04x slower                                                      |
| pyflate                 | 403 ms                                                                 | 421 ms: 1.04x slower                                                       |
| fannkuch                | 358 ms                                                                 | 378 ms: 1.06x slower                                                       |
| unpickle_pure_python    | 197 us                                                                 | 209 us: 1.06x slower                                                       |
| coverage                | 95.9 ms                                                                | 102 ms: 1.06x slower                                                       |
| scimark_sor             | 106 ms                                                                 | 121 ms: 1.14x slower                                                       |
| Geometric mean          | (ref)                                                                  | 1.01x slower                                                               |

Benchmark hidden because not significant (23): pickle_list, async_tree_io, scimark_fft, xml_etree_parse, sympy_expand, async_tree_cpu_io_mixed, async_tree_none, meteor_contest, create_gc_cycles, sympy_str, bench_mp_pool, sqlglot_optimize, async_tree_memoization, deepcopy_memo, sympy_sum, deepcopy, chaos, mypy, unpickle_list, pathlib, djangocms, json, telco
