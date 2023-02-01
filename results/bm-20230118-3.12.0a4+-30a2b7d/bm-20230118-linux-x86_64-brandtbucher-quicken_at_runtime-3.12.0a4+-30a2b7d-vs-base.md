
# Results vs. base

- fork: brandtbucher
- ref: quicken_at_runtime
- machine: linux-x86_64
- commit hash: 30a2b7d
- commit date: 2023-01-18
- overall geometric mean: 1.00x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230130-linux-x86_64-python-ea232716d3de1675478d-3.12.0a4+-ea23271 | bm-20230118-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-30a2b7d |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 252 ms                                                                 | 250 ms: 1.01x faster                                                       |
| docutils       | 2.49 sec                                                               | 2.50 sec: 1.00x slower                                                     |
| tornado_http   | 93.7 ms                                                                | 94.9 ms: 1.01x slower                                                      |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                               |

Benchmark hidden because not significant (2): chameleon, html5lib

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230130-linux-x86_64-python-ea232716d3de1675478d-3.12.0a4+-ea23271 | bm-20230118-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-30a2b7d |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 95.7 ms                                                                | 93.5 ms: 1.02x faster                                                      |
| pidigits       | 197 ms                                                                 | 197 ms: 1.00x faster                                                       |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                               |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230130-linux-x86_64-python-ea232716d3de1675478d-3.12.0a4+-ea23271 | bm-20230118-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-30a2b7d |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 128 ms                                                                 | 127 ms: 1.00x faster                                                       |
| regex_effbot   | 3.64 ms                                                                | 3.68 ms: 1.01x slower                                                      |
| regex_dna      | 210 ms                                                                 | 216 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                               |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230130-linux-x86_64-python-ea232716d3de1675478d-3.12.0a4+-ea23271 | bm-20230118-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-30a2b7d |
|----------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pickle_pure_python   | 285 us                                                                 | 282 us: 1.01x faster                                                       |
| xml_etree_generate   | 77.7 ms                                                                | 78.2 ms: 1.01x slower                                                      |
| unpickle_list        | 4.98 us                                                                | 5.01 us: 1.01x slower                                                      |
| xml_etree_process    | 53.8 ms                                                                | 54.2 ms: 1.01x slower                                                      |
| unpickle             | 13.1 us                                                                | 13.2 us: 1.01x slower                                                      |
| json_loads           | 24.1 us                                                                | 24.4 us: 1.01x slower                                                      |
| unpickle_pure_python | 197 us                                                                 | 199 us: 1.01x slower                                                       |
| xml_etree_parse      | 148 ms                                                                 | 150 ms: 1.01x slower                                                       |
| pickle               | 9.95 us                                                                | 10.2 us: 1.02x slower                                                      |
| pickle_dict          | 30.3 us                                                                | 31.2 us: 1.03x slower                                                      |
| xml_etree_iterparse  | 103 ms                                                                 | 107 ms: 1.04x slower                                                       |
| Geometric mean       | (ref)                                                                  | 1.01x slower                                                               |

Benchmark hidden because not significant (2): json_dumps, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230130-linux-x86_64-python-ea232716d3de1675478d-3.12.0a4+-ea23271 | bm-20230118-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-30a2b7d |
|------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 6.45 ms                                                                | 6.25 ms: 1.03x faster                                                      |
| python_startup         | 8.90 ms                                                                | 8.71 ms: 1.02x faster                                                      |
| Geometric mean         | (ref)                                                                  | 1.03x faster                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20230130-linux-x86_64-python-ea232716d3de1675478d-3.12.0a4+-ea23271 | bm-20230118-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-30a2b7d |
|-----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 33.4 ms                                                                | 33.0 ms: 1.01x faster                                                      |
| mako            | 9.75 ms                                                                | 9.78 ms: 1.00x slower                                                      |
| genshi_xml      | 46.8 ms                                                                | 47.1 ms: 1.01x slower                                                      |
| Geometric mean  | (ref)                                                                  | 1.00x faster                                                               |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark               | bm-20230130-linux-x86_64-python-ea232716d3de1675478d-3.12.0a4+-ea23271 | bm-20230118-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-30a2b7d |
|-------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| logging_silent          | 95.3 ns                                                                | 90.1 ns: 1.06x faster                                                      |
| chaos                   | 65.1 ms                                                                | 62.8 ms: 1.04x faster                                                      |
| generators              | 78.1 ms                                                                | 75.5 ms: 1.03x faster                                                      |
| python_startup_no_site  | 6.45 ms                                                                | 6.25 ms: 1.03x faster                                                      |
| go                      | 136 ms                                                                 | 133 ms: 1.03x faster                                                       |
| async_tree_memoization  | 658 ms                                                                 | 642 ms: 1.03x faster                                                       |
| pprint_pformat          | 1.42 sec                                                               | 1.38 sec: 1.02x faster                                                     |
| nbody                   | 95.7 ms                                                                | 93.5 ms: 1.02x faster                                                      |
| python_startup          | 8.90 ms                                                                | 8.71 ms: 1.02x faster                                                      |
| pyflate                 | 403 ms                                                                 | 396 ms: 1.02x faster                                                       |
| pprint_safe_repr        | 689 ms                                                                 | 676 ms: 1.02x faster                                                       |
| scimark_monte_carlo     | 66.7 ms                                                                | 65.5 ms: 1.02x faster                                                      |
| raytrace                | 283 ms                                                                 | 279 ms: 1.01x faster                                                       |
| hexiom                  | 5.95 ms                                                                | 5.87 ms: 1.01x faster                                                      |
| mdp                     | 2.52 sec                                                               | 2.49 sec: 1.01x faster                                                     |
| django_template         | 33.4 ms                                                                | 33.0 ms: 1.01x faster                                                      |
| deepcopy                | 328 us                                                                 | 324 us: 1.01x faster                                                       |
| coroutines              | 25.1 ms                                                                | 24.8 ms: 1.01x faster                                                      |
| scimark_sparse_mat_mult | 4.06 ms                                                                | 4.02 ms: 1.01x faster                                                      |
| pickle_pure_python      | 285 us                                                                 | 282 us: 1.01x faster                                                       |
| sympy_expand            | 456 ms                                                                 | 452 ms: 1.01x faster                                                       |
| scimark_fft             | 306 ms                                                                 | 304 ms: 1.01x faster                                                       |
| 2to3                    | 252 ms                                                                 | 250 ms: 1.01x faster                                                       |
| sympy_str               | 271 ms                                                                 | 269 ms: 1.01x faster                                                       |
| sympy_sum               | 155 ms                                                                 | 155 ms: 1.00x faster                                                       |
| deltablue               | 3.19 ms                                                                | 3.17 ms: 1.00x faster                                                      |
| regex_compile           | 128 ms                                                                 | 127 ms: 1.00x faster                                                       |
| sympy_integrate         | 19.7 ms                                                                | 19.6 ms: 1.00x faster                                                      |
| pidigits                | 197 ms                                                                 | 197 ms: 1.00x faster                                                       |
| mako                    | 9.75 ms                                                                | 9.78 ms: 1.00x slower                                                      |
| asyncio_tcp             | 493 ms                                                                 | 495 ms: 1.00x slower                                                       |
| create_gc_cycles        | 1.45 ms                                                                | 1.46 ms: 1.00x slower                                                      |
| docutils                | 2.49 sec                                                               | 2.50 sec: 1.00x slower                                                     |
| sqlglot_parse           | 1.40 ms                                                                | 1.40 ms: 1.01x slower                                                      |
| genshi_xml              | 46.8 ms                                                                | 47.1 ms: 1.01x slower                                                      |
| gc_traversal            | 4.03 ms                                                                | 4.06 ms: 1.01x slower                                                      |
| bench_thread_pool       | 775 us                                                                 | 780 us: 1.01x slower                                                       |
| xml_etree_generate      | 77.7 ms                                                                | 78.2 ms: 1.01x slower                                                      |
| unpickle_list           | 4.98 us                                                                | 5.01 us: 1.01x slower                                                      |
| xml_etree_process       | 53.8 ms                                                                | 54.2 ms: 1.01x slower                                                      |
| logging_format          | 6.35 us                                                                | 6.40 us: 1.01x slower                                                      |
| unpickle                | 13.1 us                                                                | 13.2 us: 1.01x slower                                                      |
| regex_effbot            | 3.64 ms                                                                | 3.68 ms: 1.01x slower                                                      |
| sqlite_synth            | 2.56 us                                                                | 2.58 us: 1.01x slower                                                      |
| json_loads              | 24.1 us                                                                | 24.4 us: 1.01x slower                                                      |
| dulwich_log             | 62.3 ms                                                                | 63.0 ms: 1.01x slower                                                      |
| unpickle_pure_python    | 197 us                                                                 | 199 us: 1.01x slower                                                       |
| xml_etree_parse         | 148 ms                                                                 | 150 ms: 1.01x slower                                                       |
| tornado_http            | 93.7 ms                                                                | 94.9 ms: 1.01x slower                                                      |
| logging_simple          | 5.72 us                                                                | 5.80 us: 1.01x slower                                                      |
| deepcopy_reduce         | 2.90 us                                                                | 2.94 us: 1.02x slower                                                      |
| scimark_sor             | 106 ms                                                                 | 108 ms: 1.02x slower                                                       |
| pathlib                 | 17.7 ms                                                                | 18.0 ms: 1.02x slower                                                      |
| pickle                  | 9.95 us                                                                | 10.2 us: 1.02x slower                                                      |
| thrift                  | 736 us                                                                 | 752 us: 1.02x slower                                                       |
| richards                | 42.6 ms                                                                | 43.7 ms: 1.03x slower                                                      |
| spectral_norm           | 96.7 ms                                                                | 99.4 ms: 1.03x slower                                                      |
| pickle_dict             | 30.3 us                                                                | 31.2 us: 1.03x slower                                                      |
| regex_dna               | 210 ms                                                                 | 216 ms: 1.03x slower                                                       |
| xml_etree_iterparse     | 103 ms                                                                 | 107 ms: 1.04x slower                                                       |
| meteor_contest          | 106 ms                                                                 | 111 ms: 1.05x slower                                                       |
| unpack_sequence         | 42.3 ns                                                                | 45.1 ns: 1.06x slower                                                      |
| coverage                | 95.9 ms                                                                | 102 ms: 1.07x slower                                                       |
| Geometric mean          | (ref)                                                                  | 1.00x slower                                                               |

Benchmark hidden because not significant (28): telco, async_tree_cpu_io_mixed, deepcopy_memo, async_tree_none, pycparser, float, crypto_pyaes, fannkuch, async_generators, aiohttp, bench_mp_pool, regex_v8, sqlglot_normalize, json, djangocms, json_dumps, sqlglot_optimize, gunicorn, nqueens, sqlglot_transpile, chameleon, mypy, genshi_text, async_tree_io, html5lib, scimark_lu, dask, pickle_list
