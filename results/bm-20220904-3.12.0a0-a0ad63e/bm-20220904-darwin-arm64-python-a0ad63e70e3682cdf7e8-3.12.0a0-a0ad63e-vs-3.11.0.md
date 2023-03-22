
# Results vs. 3.11.0

- fork: python
- ref: a0ad63e70e3682cdf7e8
- machine: darwin-arm64
- commit hash: a0ad63e
- commit date: 2022-09-04
- overall geometric mean: 1.01x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220904-darwin-arm64-python-a0ad63e70e3682cdf7e8-3.12.0a0-a0ad63e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 161 ms                                                 | 185 ms: 1.15x slower                                                  |
| chameleon      | 4.57 ms                                                | 4.59 ms: 1.00x slower                                                 |
| docutils       | 1.47 sec                                               | 1.48 sec: 1.01x slower                                                |
| html5lib       | 34.7 ms                                                | 36.4 ms: 1.05x slower                                                 |
| Geometric mean | (ref)                                                  | 1.03x slower                                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220904-darwin-arm64-python-a0ad63e70e3682cdf7e8-3.12.0a0-a0ad63e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 53.0 ms                                                | 51.3 ms: 1.03x faster                                                 |
| nbody          | 65.5 ms                                                | 64.0 ms: 1.02x faster                                                 |
| pidigits       | 281 ms                                                 | 282 ms: 1.01x slower                                                  |
| Geometric mean | (ref)                                                  | 1.02x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220904-darwin-arm64-python-a0ad63e70e3682cdf7e8-3.12.0a0-a0ad63e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 76.7 ms                                                | 75.3 ms: 1.02x faster                                                 |
| regex_dna      | 152 ms                                                 | 151 ms: 1.00x faster                                                  |
| regex_v8       | 16.2 ms                                                | 16.4 ms: 1.01x slower                                                 |
| regex_effbot   | 2.63 ms                                                | 2.72 ms: 1.03x slower                                                 |
| Geometric mean | (ref)                                                  | 1.01x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220904-darwin-arm64-python-a0ad63e70e3682cdf7e8-3.12.0a0-a0ad63e |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| json_dumps           | 7.72 ms                                                | 6.10 ms: 1.26x faster                                                 |
| xml_etree_parse      | 106 ms                                                 | 95.9 ms: 1.11x faster                                                 |
| xml_etree_iterparse  | 69.2 ms                                                | 64.5 ms: 1.07x faster                                                 |
| xml_etree_generate   | 48.8 ms                                                | 47.2 ms: 1.03x faster                                                 |
| xml_etree_process    | 35.2 ms                                                | 34.5 ms: 1.02x faster                                                 |
| unpickle_list        | 2.63 us                                                | 2.58 us: 1.02x faster                                                 |
| pickle_dict          | 17.9 us                                                | 18.0 us: 1.00x slower                                                 |
| json_loads           | 16.1 us                                                | 16.2 us: 1.01x slower                                                 |
| unpickle_pure_python | 159 us                                                 | 160 us: 1.01x slower                                                  |
| pickle_list          | 2.81 us                                                | 2.85 us: 1.02x slower                                                 |
| pickle               | 7.17 us                                                | 7.59 us: 1.06x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                          |

Benchmark hidden because not significant (2): unpickle, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220904-darwin-arm64-python-a0ad63e70e3682cdf7e8-3.12.0a0-a0ad63e |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 9.31 ms                                                | 7.16 ms: 1.30x faster                                                 |
| python_startup         | 11.5 ms                                                | 9.07 ms: 1.27x faster                                                 |
| Geometric mean         | (ref)                                                  | 1.29x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220904-darwin-arm64-python-a0ad63e70e3682cdf7e8-3.12.0a0-a0ad63e |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 8.49 ms                                                | 7.97 ms: 1.07x faster                                                 |
| genshi_text     | 15.3 ms                                                | 15.1 ms: 1.01x faster                                                 |
| django_template | 21.0 ms                                                | 20.9 ms: 1.01x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.02x faster                                                          |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark               | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220904-darwin-arm64-python-a0ad63e70e3682cdf7e8-3.12.0a0-a0ad63e |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pathlib                 | 27.8 ms                                                | 20.8 ms: 1.34x faster                                                 |
| python_startup_no_site  | 9.31 ms                                                | 7.16 ms: 1.30x faster                                                 |
| python_startup          | 11.5 ms                                                | 9.07 ms: 1.27x faster                                                 |
| json_dumps              | 7.72 ms                                                | 6.10 ms: 1.26x faster                                                 |
| scimark_sparse_mat_mult | 3.20 ms                                                | 2.80 ms: 1.14x faster                                                 |
| xml_etree_parse         | 106 ms                                                 | 95.9 ms: 1.11x faster                                                 |
| flaskblogging           | 2.42 ms                                                | 2.22 ms: 1.09x faster                                                 |
| coverage                | 58.6 ms                                                | 54.3 ms: 1.08x faster                                                 |
| xml_etree_iterparse     | 69.2 ms                                                | 64.5 ms: 1.07x faster                                                 |
| mako                    | 8.49 ms                                                | 7.97 ms: 1.07x faster                                                 |
| deepcopy_memo           | 26.3 us                                                | 24.8 us: 1.06x faster                                                 |
| bench_mp_pool           | 43.2 ms                                                | 40.9 ms: 1.06x faster                                                 |
| logging_silent          | 68.0 ns                                                | 64.5 ns: 1.05x faster                                                 |
| bench_thread_pool       | 473 us                                                 | 449 us: 1.05x faster                                                  |
| nqueens                 | 61.8 ms                                                | 58.7 ms: 1.05x faster                                                 |
| deepcopy                | 224 us                                                 | 215 us: 1.04x faster                                                  |
| xml_etree_generate      | 48.8 ms                                                | 47.2 ms: 1.03x faster                                                 |
| deepcopy_reduce         | 1.91 us                                                | 1.85 us: 1.03x faster                                                 |
| float                   | 53.0 ms                                                | 51.3 ms: 1.03x faster                                                 |
| sqlalchemy_imperative   | 7.31 ms                                                | 7.12 ms: 1.03x faster                                                 |
| sympy_sum               | 86.0 ms                                                | 84.0 ms: 1.02x faster                                                 |
| pylint                  | 271 ms                                                 | 264 ms: 1.02x faster                                                  |
| nbody                   | 65.5 ms                                                | 64.0 ms: 1.02x faster                                                 |
| xml_etree_process       | 35.2 ms                                                | 34.5 ms: 1.02x faster                                                 |
| unpickle_list           | 2.63 us                                                | 2.58 us: 1.02x faster                                                 |
| sqlalchemy_declarative  | 62.7 ms                                                | 61.5 ms: 1.02x faster                                                 |
| regex_compile           | 76.7 ms                                                | 75.3 ms: 1.02x faster                                                 |
| unpack_sequence         | 33.6 ns                                                | 33.0 ns: 1.02x faster                                                 |
| telco                   | 3.39 ms                                                | 3.34 ms: 1.02x faster                                                 |
| spectral_norm           | 72.8 ms                                                | 71.7 ms: 1.01x faster                                                 |
| dulwich_log             | 29.9 ms                                                | 29.5 ms: 1.01x faster                                                 |
| scimark_fft             | 199 ms                                                 | 197 ms: 1.01x faster                                                  |
| crypto_pyaes            | 51.7 ms                                                | 51.1 ms: 1.01x faster                                                 |
| genshi_text             | 15.3 ms                                                | 15.1 ms: 1.01x faster                                                 |
| async_tree_cpu_io_mixed | 534 ms                                                 | 530 ms: 1.01x faster                                                  |
| django_template         | 21.0 ms                                                | 20.9 ms: 1.01x faster                                                 |
| regex_dna               | 152 ms                                                 | 151 ms: 1.00x faster                                                  |
| sqlglot_normalize       | 171 ms                                                 | 172 ms: 1.00x slower                                                  |
| chameleon               | 4.57 ms                                                | 4.59 ms: 1.00x slower                                                 |
| pickle_dict             | 17.9 us                                                | 18.0 us: 1.00x slower                                                 |
| docutils                | 1.47 sec                                               | 1.48 sec: 1.01x slower                                                |
| pidigits                | 281 ms                                                 | 282 ms: 1.01x slower                                                  |
| mdp                     | 1.54 sec                                               | 1.55 sec: 1.01x slower                                                |
| pprint_safe_repr        | 465 ms                                                 | 468 ms: 1.01x slower                                                  |
| json_loads              | 16.1 us                                                | 16.2 us: 1.01x slower                                                 |
| unpickle_pure_python    | 159 us                                                 | 160 us: 1.01x slower                                                  |
| scimark_lu              | 72.1 ms                                                | 72.7 ms: 1.01x slower                                                 |
| deltablue               | 2.81 ms                                                | 2.84 ms: 1.01x slower                                                 |
| generators              | 28.8 ms                                                | 29.1 ms: 1.01x slower                                                 |
| regex_v8                | 16.2 ms                                                | 16.4 ms: 1.01x slower                                                 |
| sympy_expand            | 243 ms                                                 | 247 ms: 1.01x slower                                                  |
| pickle_list             | 2.81 us                                                | 2.85 us: 1.02x slower                                                 |
| thrift                  | 433 us                                                 | 441 us: 1.02x slower                                                  |
| sqlglot_optimize        | 31.2 ms                                                | 31.7 ms: 1.02x slower                                                 |
| json                    | 2.77 ms                                                | 2.82 ms: 1.02x slower                                                 |
| pycparser               | 697 ms                                                 | 711 ms: 1.02x slower                                                  |
| async_generators        | 195 ms                                                 | 199 ms: 1.02x slower                                                  |
| raytrace                | 207 ms                                                 | 211 ms: 1.02x slower                                                  |
| hexiom                  | 4.73 ms                                                | 4.84 ms: 1.02x slower                                                 |
| fannkuch                | 261 ms                                                 | 268 ms: 1.03x slower                                                  |
| regex_effbot            | 2.63 ms                                                | 2.72 ms: 1.03x slower                                                 |
| logging_simple          | 3.50 us                                                | 3.63 us: 1.04x slower                                                 |
| logging_format          | 3.78 us                                                | 3.92 us: 1.04x slower                                                 |
| sqlglot_transpile       | 1.12 ms                                                | 1.16 ms: 1.04x slower                                                 |
| richards                | 32.2 ms                                                | 33.4 ms: 1.04x slower                                                 |
| async_tree_io           | 706 ms                                                 | 734 ms: 1.04x slower                                                  |
| meteor_contest          | 73.8 ms                                                | 77.0 ms: 1.04x slower                                                 |
| sqlglot_parse           | 957 us                                                 | 1.00 ms: 1.05x slower                                                 |
| html5lib                | 34.7 ms                                                | 36.4 ms: 1.05x slower                                                 |
| pickle                  | 7.17 us                                                | 7.59 us: 1.06x slower                                                 |
| go                      | 109 ms                                                 | 117 ms: 1.08x slower                                                  |
| coroutines              | 17.7 ms                                                | 19.3 ms: 1.09x slower                                                 |
| sqlite_synth            | 1.27 us                                                | 1.40 us: 1.10x slower                                                 |
| pyflate                 | 311 ms                                                 | 345 ms: 1.11x slower                                                  |
| async_tree_memoization  | 336 ms                                                 | 381 ms: 1.14x slower                                                  |
| 2to3                    | 161 ms                                                 | 185 ms: 1.15x slower                                                  |
| scimark_monte_carlo     | 46.4 ms                                                | 53.8 ms: 1.16x slower                                                 |
| scimark_sor             | 83.0 ms                                                | 99.0 ms: 1.19x slower                                                 |
| Geometric mean          | (ref)                                                  | 1.01x faster                                                          |

Benchmark hidden because not significant (9): tornado_http, unpickle, async_tree_none, pickle_pure_python, sympy_integrate, pprint_pformat, sympy_str, chaos, genshi_xml
Ignored benchmarks (8) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp, comprehensions, create_gc_cycles, dask, gc_traversal, gunicorn, mypy2
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20220904-3.12.0a0-a0ad63e/bm-20220904-darwin-arm64-python-a0ad63e70e3682cdf7e8-3.12.0a0-a0ad63e.json: mypy
