
# Results vs. 3.11.0

- fork: python
- ref: 728e42fcf51cbb2108ca
- machine: darwin-arm64
- commit hash: 728e42f
- commit date: 2022-11-06
- overall geometric mean: 1.03x slower \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20221106-darwin-arm64-python-728e42fcf51cbb2108ca-3.12.0a1+-728e42f |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 161 ms                                                 | 187 ms: 1.16x slower                                                   |
| chameleon      | 4.57 ms                                                | 5.13 ms: 1.12x slower                                                  |
| docutils       | 1.47 sec                                               | 1.50 sec: 1.02x slower                                                 |
| html5lib       | 34.7 ms                                                | 37.5 ms: 1.08x slower                                                  |
| Geometric mean | (ref)                                                  | 1.07x slower                                                           |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20221106-darwin-arm64-python-728e42fcf51cbb2108ca-3.12.0a1+-728e42f |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 65.5 ms                                                | 65.9 ms: 1.01x slower                                                  |
| pidigits       | 281 ms                                                 | 282 ms: 1.01x slower                                                   |
| float          | 53.0 ms                                                | 57.3 ms: 1.08x slower                                                  |
| Geometric mean | (ref)                                                  | 1.03x slower                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20221106-darwin-arm64-python-728e42fcf51cbb2108ca-3.12.0a1+-728e42f |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_dna      | 152 ms                                                 | 149 ms: 1.02x faster                                                   |
| regex_v8       | 16.2 ms                                                | 16.1 ms: 1.00x faster                                                  |
| regex_compile  | 76.7 ms                                                | 77.7 ms: 1.01x slower                                                  |
| Geometric mean | (ref)                                                  | 1.00x faster                                                           |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20221106-darwin-arm64-python-728e42fcf51cbb2108ca-3.12.0a1+-728e42f |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| json_dumps           | 7.72 ms                                                | 6.15 ms: 1.25x faster                                                  |
| xml_etree_parse      | 106 ms                                                 | 93.3 ms: 1.14x faster                                                  |
| xml_etree_iterparse  | 69.2 ms                                                | 65.0 ms: 1.06x faster                                                  |
| unpickle_list        | 2.63 us                                                | 2.60 us: 1.01x faster                                                  |
| pickle_dict          | 17.9 us                                                | 18.0 us: 1.00x slower                                                  |
| unpickle             | 9.70 us                                                | 9.86 us: 1.02x slower                                                  |
| json_loads           | 16.1 us                                                | 16.4 us: 1.02x slower                                                  |
| pickle_list          | 2.81 us                                                | 2.88 us: 1.03x slower                                                  |
| xml_etree_generate   | 48.8 ms                                                | 50.5 ms: 1.03x slower                                                  |
| xml_etree_process    | 35.2 ms                                                | 36.8 ms: 1.05x slower                                                  |
| unpickle_pure_python | 159 us                                                 | 167 us: 1.05x slower                                                   |
| pickle               | 7.17 us                                                | 7.55 us: 1.05x slower                                                  |
| pickle_pure_python   | 199 us                                                 | 222 us: 1.12x slower                                                   |
| Geometric mean       | (ref)                                                  | 1.01x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20221106-darwin-arm64-python-728e42fcf51cbb2108ca-3.12.0a1+-728e42f |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 9.31 ms                                                | 7.38 ms: 1.26x faster                                                  |
| python_startup         | 11.5 ms                                                | 9.32 ms: 1.24x faster                                                  |
| Geometric mean         | (ref)                                                  | 1.25x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20221106-darwin-arm64-python-728e42fcf51cbb2108ca-3.12.0a1+-728e42f |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 8.49 ms                                                | 8.59 ms: 1.01x slower                                                  |
| django_template | 21.0 ms                                                | 22.2 ms: 1.05x slower                                                  |
| genshi_text     | 15.3 ms                                                | 16.2 ms: 1.06x slower                                                  |
| genshi_xml      | 29.8 ms                                                | 32.4 ms: 1.09x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.05x slower                                                           |

All benchmarks:
===============

| Benchmark               | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20221106-darwin-arm64-python-728e42fcf51cbb2108ca-3.12.0a1+-728e42f |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pathlib                 | 27.8 ms                                                | 20.8 ms: 1.34x faster                                                  |
| python_startup_no_site  | 9.31 ms                                                | 7.38 ms: 1.26x faster                                                  |
| json_dumps              | 7.72 ms                                                | 6.15 ms: 1.25x faster                                                  |
| python_startup          | 11.5 ms                                                | 9.32 ms: 1.24x faster                                                  |
| scimark_sparse_mat_mult | 3.20 ms                                                | 2.76 ms: 1.16x faster                                                  |
| xml_etree_parse         | 106 ms                                                 | 93.3 ms: 1.14x faster                                                  |
| coverage                | 58.6 ms                                                | 53.1 ms: 1.10x faster                                                  |
| xml_etree_iterparse     | 69.2 ms                                                | 65.0 ms: 1.06x faster                                                  |
| pylint                  | 271 ms                                                 | 257 ms: 1.05x faster                                                   |
| nqueens                 | 61.8 ms                                                | 59.3 ms: 1.04x faster                                                  |
| logging_silent          | 68.0 ns                                                | 65.6 ns: 1.04x faster                                                  |
| generators              | 28.8 ms                                                | 28.1 ms: 1.03x faster                                                  |
| bench_thread_pool       | 473 us                                                 | 463 us: 1.02x faster                                                   |
| regex_dna               | 152 ms                                                 | 149 ms: 1.02x faster                                                   |
| unpickle_list           | 2.63 us                                                | 2.60 us: 1.01x faster                                                  |
| spectral_norm           | 72.8 ms                                                | 71.9 ms: 1.01x faster                                                  |
| scimark_lu              | 72.1 ms                                                | 71.2 ms: 1.01x faster                                                  |
| dulwich_log             | 29.9 ms                                                | 29.7 ms: 1.01x faster                                                  |
| richards                | 32.2 ms                                                | 32.0 ms: 1.00x faster                                                  |
| regex_v8                | 16.2 ms                                                | 16.1 ms: 1.00x faster                                                  |
| scimark_fft             | 199 ms                                                 | 200 ms: 1.00x slower                                                   |
| pickle_dict             | 17.9 us                                                | 18.0 us: 1.00x slower                                                  |
| nbody                   | 65.5 ms                                                | 65.9 ms: 1.01x slower                                                  |
| pidigits                | 281 ms                                                 | 282 ms: 1.01x slower                                                   |
| mdp                     | 1.54 sec                                               | 1.55 sec: 1.01x slower                                                 |
| mako                    | 8.49 ms                                                | 8.59 ms: 1.01x slower                                                  |
| regex_compile           | 76.7 ms                                                | 77.7 ms: 1.01x slower                                                  |
| telco                   | 3.39 ms                                                | 3.44 ms: 1.01x slower                                                  |
| deltablue               | 2.81 ms                                                | 2.85 ms: 1.02x slower                                                  |
| unpickle                | 9.70 us                                                | 9.86 us: 1.02x slower                                                  |
| sqlglot_normalize       | 171 ms                                                 | 175 ms: 1.02x slower                                                   |
| json_loads              | 16.1 us                                                | 16.4 us: 1.02x slower                                                  |
| pycparser               | 697 ms                                                 | 711 ms: 1.02x slower                                                   |
| docutils                | 1.47 sec                                               | 1.50 sec: 1.02x slower                                                 |
| thrift                  | 433 us                                                 | 443 us: 1.02x slower                                                   |
| sympy_sum               | 86.0 ms                                                | 88.0 ms: 1.02x slower                                                  |
| async_tree_cpu_io_mixed | 534 ms                                                 | 547 ms: 1.02x slower                                                   |
| pickle_list             | 2.81 us                                                | 2.88 us: 1.03x slower                                                  |
| sqlglot_optimize        | 31.2 ms                                                | 32.0 ms: 1.03x slower                                                  |
| async_tree_none         | 285 ms                                                 | 294 ms: 1.03x slower                                                   |
| json                    | 2.77 ms                                                | 2.86 ms: 1.03x slower                                                  |
| xml_etree_generate      | 48.8 ms                                                | 50.5 ms: 1.03x slower                                                  |
| async_generators        | 195 ms                                                 | 202 ms: 1.04x slower                                                   |
| fannkuch                | 261 ms                                                 | 270 ms: 1.04x slower                                                   |
| raytrace                | 207 ms                                                 | 215 ms: 1.04x slower                                                   |
| hexiom                  | 4.73 ms                                                | 4.91 ms: 1.04x slower                                                  |
| async_tree_io           | 706 ms                                                 | 736 ms: 1.04x slower                                                   |
| chaos                   | 49.5 ms                                                | 51.6 ms: 1.04x slower                                                  |
| xml_etree_process       | 35.2 ms                                                | 36.8 ms: 1.05x slower                                                  |
| sympy_expand            | 243 ms                                                 | 255 ms: 1.05x slower                                                   |
| sympy_str               | 152 ms                                                 | 159 ms: 1.05x slower                                                   |
| unpickle_pure_python    | 159 us                                                 | 167 us: 1.05x slower                                                   |
| pickle                  | 7.17 us                                                | 7.55 us: 1.05x slower                                                  |
| django_template         | 21.0 ms                                                | 22.2 ms: 1.05x slower                                                  |
| sympy_integrate         | 11.5 ms                                                | 12.1 ms: 1.06x slower                                                  |
| sqlglot_transpile       | 1.12 ms                                                | 1.19 ms: 1.06x slower                                                  |
| sqlglot_parse           | 957 us                                                 | 1.01 ms: 1.06x slower                                                  |
| genshi_text             | 15.3 ms                                                | 16.2 ms: 1.06x slower                                                  |
| coroutines              | 17.7 ms                                                | 19.1 ms: 1.08x slower                                                  |
| logging_simple          | 3.50 us                                                | 3.77 us: 1.08x slower                                                  |
| html5lib                | 34.7 ms                                                | 37.5 ms: 1.08x slower                                                  |
| float                   | 53.0 ms                                                | 57.3 ms: 1.08x slower                                                  |
| logging_format          | 3.78 us                                                | 4.09 us: 1.08x slower                                                  |
| genshi_xml              | 29.8 ms                                                | 32.4 ms: 1.09x slower                                                  |
| meteor_contest          | 73.8 ms                                                | 80.5 ms: 1.09x slower                                                  |
| pprint_safe_repr        | 465 ms                                                 | 514 ms: 1.11x slower                                                   |
| pprint_pformat          | 950 ms                                                 | 1.05 sec: 1.11x slower                                                 |
| go                      | 109 ms                                                 | 121 ms: 1.11x slower                                                   |
| pickle_pure_python      | 199 us                                                 | 222 us: 1.12x slower                                                   |
| chameleon               | 4.57 ms                                                | 5.13 ms: 1.12x slower                                                  |
| sqlite_synth            | 1.27 us                                                | 1.45 us: 1.14x slower                                                  |
| pyflate                 | 311 ms                                                 | 355 ms: 1.14x slower                                                   |
| 2to3                    | 161 ms                                                 | 187 ms: 1.16x slower                                                   |
| deepcopy                | 224 us                                                 | 263 us: 1.17x slower                                                   |
| scimark_monte_carlo     | 46.4 ms                                                | 54.9 ms: 1.18x slower                                                  |
| deepcopy_reduce         | 1.91 us                                                | 2.28 us: 1.19x slower                                                  |
| deepcopy_memo           | 26.3 us                                                | 32.1 us: 1.22x slower                                                  |
| scimark_sor             | 83.0 ms                                                | 103 ms: 1.24x slower                                                   |
| unpack_sequence         | 33.6 ns                                                | 52.1 ns: 1.55x slower                                                  |
| Geometric mean          | (ref)                                                  | 1.03x slower                                                           |

Benchmark hidden because not significant (5): tornado_http, bench_mp_pool, async_tree_memoization, crypto_pyaes, regex_effbot
Ignored benchmarks (11) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp, comprehensions, create_gc_cycles, dask, flaskblogging, gc_traversal, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20221106-3.12.0a1+-728e42f/bm-20221106-darwin-arm64-python-728e42fcf51cbb2108ca-3.12.0a1+-728e42f.json: mypy
