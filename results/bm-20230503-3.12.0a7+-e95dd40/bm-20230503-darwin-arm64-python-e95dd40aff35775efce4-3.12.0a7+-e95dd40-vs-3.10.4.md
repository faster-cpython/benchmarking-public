
# Results vs. 3.10.4

- fork: python
- ref: e95dd40aff35775efce4
- machine: darwin-arm64
- commit hash: e95dd40
- commit date: 2023-05-03
- overall geometric mean: 1.16x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.09x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230503-darwin-arm64-python-e95dd40aff35775efce4-3.12.0a7+-e95dd40 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 202 ms                                                 | 173 ms: 1.17x faster                                                   |
| docutils       | 1.78 sec                                               | 1.56 sec: 1.14x faster                                                 |
| tornado_http   | 91.9 ms                                                | 71.5 ms: 1.29x faster                                                  |
| Geometric mean | (ref)                                                  | 1.20x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230503-darwin-arm64-python-e95dd40aff35775efce4-3.12.0a7+-e95dd40 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 94.1 ms                                                | 69.7 ms: 1.35x faster                                                  |
| float          | 72.3 ms                                                | 58.9 ms: 1.23x faster                                                  |
| pidigits       | 282 ms                                                 | 281 ms: 1.00x faster                                                   |
| Geometric mean | (ref)                                                  | 1.19x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230503-darwin-arm64-python-e95dd40aff35775efce4-3.12.0a7+-e95dd40 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 96.6 ms                                                | 78.7 ms: 1.23x faster                                                  |
| regex_v8       | 17.5 ms                                                | 16.3 ms: 1.07x faster                                                  |
| regex_dna      | 160 ms                                                 | 150 ms: 1.07x faster                                                   |
| regex_effbot   | 2.45 ms                                                | 2.69 ms: 1.10x slower                                                  |
| Geometric mean | (ref)                                                  | 1.06x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230503-darwin-arm64-python-e95dd40aff35775efce4-3.12.0a7+-e95dd40 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_pure_python   | 284 us                                                 | 194 us: 1.46x faster                                                   |
| unpickle_pure_python | 203 us                                                 | 151 us: 1.35x faster                                                   |
| json_dumps           | 8.38 ms                                                | 6.92 ms: 1.21x faster                                                  |
| xml_etree_process    | 45.1 ms                                                | 40.2 ms: 1.12x faster                                                  |
| xml_etree_parse      | 107 ms                                                 | 108 ms: 1.01x slower                                                   |
| unpickle             | 9.77 us                                                | 10.1 us: 1.03x slower                                                  |
| xml_etree_iterparse  | 72.6 ms                                                | 75.1 ms: 1.03x slower                                                  |
| json_loads           | 16.9 us                                                | 17.9 us: 1.06x slower                                                  |
| pickle_dict          | 17.8 us                                                | 19.0 us: 1.07x slower                                                  |
| xml_etree_generate   | 54.3 ms                                                | 58.0 ms: 1.07x slower                                                  |
| pickle_list          | 2.83 us                                                | 3.05 us: 1.08x slower                                                  |
| pickle               | 7.36 us                                                | 7.95 us: 1.08x slower                                                  |
| unpickle_list        | 2.66 us                                                | 3.19 us: 1.20x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230503-darwin-arm64-python-e95dd40aff35775efce4-3.12.0a7+-e95dd40 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 12.6 ms                                                | 12.5 ms: 1.01x faster                                                  |
| python_startup_no_site | 9.73 ms                                                | 10.4 ms: 1.07x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.03x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230503-darwin-arm64-python-e95dd40aff35775efce4-3.12.0a7+-e95dd40 |
|-----------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako      | 10.5 ms                                                | 7.81 ms: 1.34x faster                                                  |

All benchmarks:
===============

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230503-darwin-arm64-python-e95dd40aff35775efce4-3.12.0a7+-e95dd40 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| deltablue               | 5.15 ms                                                | 2.47 ms: 2.08x faster                                                  |
| logging_silent          | 119 ns                                                 | 71.0 ns: 1.68x faster                                                  |
| asyncio_tcp             | 673 ms                                                 | 420 ms: 1.60x faster                                                   |
| richards                | 51.4 ms                                                | 32.4 ms: 1.59x faster                                                  |
| go                      | 165 ms                                                 | 109 ms: 1.51x faster                                                   |
| sqlglot_parse           | 1.33 ms                                                | 903 us: 1.47x faster                                                   |
| scimark_sor             | 127 ms                                                 | 86.4 ms: 1.47x faster                                                  |
| async_tree_memoization  | 493 ms                                                 | 337 ms: 1.46x faster                                                   |
| hexiom                  | 6.32 ms                                                | 4.32 ms: 1.46x faster                                                  |
| pickle_pure_python      | 284 us                                                 | 194 us: 1.46x faster                                                   |
| async_tree_io           | 1.02 sec                                               | 712 ms: 1.43x faster                                                   |
| sqlglot_transpile       | 1.54 ms                                                | 1.08 ms: 1.42x faster                                                  |
| async_tree_none         | 402 ms                                                 | 285 ms: 1.41x faster                                                   |
| crypto_pyaes            | 78.0 ms                                                | 55.9 ms: 1.40x faster                                                  |
| scimark_monte_carlo     | 72.2 ms                                                | 52.1 ms: 1.39x faster                                                  |
| chaos                   | 66.8 ms                                                | 48.4 ms: 1.38x faster                                                  |
| unpack_sequence         | 38.7 ns                                                | 28.1 ns: 1.38x faster                                                  |
| nbody                   | 94.1 ms                                                | 69.7 ms: 1.35x faster                                                  |
| unpickle_pure_python    | 203 us                                                 | 151 us: 1.35x faster                                                   |
| mako                    | 10.5 ms                                                | 7.81 ms: 1.34x faster                                                  |
| scimark_lu              | 110 ms                                                 | 82.0 ms: 1.34x faster                                                  |
| generators              | 32.9 ms                                                | 24.9 ms: 1.32x faster                                                  |
| pyflate                 | 453 ms                                                 | 343 ms: 1.32x faster                                                   |
| raytrace                | 328 ms                                                 | 250 ms: 1.31x faster                                                   |
| deepcopy_memo           | 34.5 us                                                | 26.4 us: 1.31x faster                                                  |
| pycparser               | 915 ms                                                 | 701 ms: 1.31x faster                                                   |
| tornado_http            | 91.9 ms                                                | 71.5 ms: 1.29x faster                                                  |
| create_gc_cycles        | 876 us                                                 | 695 us: 1.26x faster                                                   |
| logging_format          | 5.01 us                                                | 4.00 us: 1.25x faster                                                  |
| async_tree_cpu_io_mixed | 670 ms                                                 | 536 ms: 1.25x faster                                                   |
| logging_simple          | 4.63 us                                                | 3.72 us: 1.25x faster                                                  |
| regex_compile           | 96.6 ms                                                | 78.7 ms: 1.23x faster                                                  |
| float                   | 72.3 ms                                                | 58.9 ms: 1.23x faster                                                  |
| sqlalchemy_imperative   | 9.03 ms                                                | 7.37 ms: 1.23x faster                                                  |
| spectral_norm           | 96.4 ms                                                | 79.0 ms: 1.22x faster                                                  |
| json_dumps              | 8.38 ms                                                | 6.92 ms: 1.21x faster                                                  |
| dulwich_log             | 37.1 ms                                                | 30.7 ms: 1.21x faster                                                  |
| pprint_pformat          | 1.24 sec                                               | 1.04 sec: 1.20x faster                                                 |
| pprint_safe_repr        | 609 ms                                                 | 511 ms: 1.19x faster                                                   |
| 2to3                    | 202 ms                                                 | 173 ms: 1.17x faster                                                   |
| deepcopy                | 278 us                                                 | 239 us: 1.16x faster                                                   |
| mypy2                   | 308 ms                                                 | 266 ms: 1.16x faster                                                   |
| docutils                | 1.78 sec                                               | 1.56 sec: 1.14x faster                                                 |
| fannkuch                | 317 ms                                                 | 279 ms: 1.14x faster                                                   |
| xml_etree_process       | 45.1 ms                                                | 40.2 ms: 1.12x faster                                                  |
| deepcopy_reduce         | 2.38 us                                                | 2.13 us: 1.12x faster                                                  |
| coroutines              | 20.2 ms                                                | 18.0 ms: 1.12x faster                                                  |
| bench_thread_pool       | 548 us                                                 | 499 us: 1.10x faster                                                   |
| scimark_fft             | 232 ms                                                 | 214 ms: 1.09x faster                                                   |
| sqlalchemy_declarative  | 74.8 ms                                                | 69.2 ms: 1.08x faster                                                  |
| regex_v8                | 17.5 ms                                                | 16.3 ms: 1.07x faster                                                  |
| nqueens                 | 68.1 ms                                                | 63.4 ms: 1.07x faster                                                  |
| regex_dna               | 160 ms                                                 | 150 ms: 1.07x faster                                                   |
| mdp                     | 1.67 sec                                               | 1.58 sec: 1.06x faster                                                 |
| scimark_sparse_mat_mult | 3.47 ms                                                | 3.31 ms: 1.05x faster                                                  |
| sqlglot_optimize        | 38.0 ms                                                | 36.5 ms: 1.04x faster                                                  |
| json                    | 3.10 ms                                                | 3.03 ms: 1.02x faster                                                  |
| pathlib                 | 28.8 ms                                                | 28.3 ms: 1.02x faster                                                  |
| meteor_contest          | 78.6 ms                                                | 77.4 ms: 1.02x faster                                                  |
| python_startup          | 12.6 ms                                                | 12.5 ms: 1.01x faster                                                  |
| pidigits                | 282 ms                                                 | 281 ms: 1.00x faster                                                   |
| gc_traversal            | 2.40 ms                                                | 2.42 ms: 1.01x slower                                                  |
| xml_etree_parse         | 107 ms                                                 | 108 ms: 1.01x slower                                                   |
| sqlglot_normalize       | 197 ms                                                 | 200 ms: 1.02x slower                                                   |
| comprehensions          | 17.7 us                                                | 18.0 us: 1.02x slower                                                  |
| unpickle                | 9.77 us                                                | 10.1 us: 1.03x slower                                                  |
| xml_etree_iterparse     | 72.6 ms                                                | 75.1 ms: 1.03x slower                                                  |
| json_loads              | 16.9 us                                                | 17.9 us: 1.06x slower                                                  |
| pickle_dict             | 17.8 us                                                | 19.0 us: 1.07x slower                                                  |
| xml_etree_generate      | 54.3 ms                                                | 58.0 ms: 1.07x slower                                                  |
| python_startup_no_site  | 9.73 ms                                                | 10.4 ms: 1.07x slower                                                  |
| pickle_list             | 2.83 us                                                | 3.05 us: 1.08x slower                                                  |
| pickle                  | 7.36 us                                                | 7.95 us: 1.08x slower                                                  |
| sqlite_synth            | 1.47 us                                                | 1.60 us: 1.09x slower                                                  |
| telco                   | 3.68 ms                                                | 4.03 ms: 1.10x slower                                                  |
| regex_effbot            | 2.45 ms                                                | 2.69 ms: 1.10x slower                                                  |
| bench_mp_pool           | 41.0 ms                                                | 48.4 ms: 1.18x slower                                                  |
| unpickle_list           | 2.66 us                                                | 3.19 us: 1.20x slower                                                  |
| dask                    | 258 ms                                                 | 334 ms: 1.30x slower                                                   |
| async_generators        | 233 ms                                                 | 315 ms: 1.35x slower                                                   |
| coverage                | 40.8 ms                                                | 58.8 ms: 1.44x slower                                                  |
| Geometric mean          | (ref)                                                  | 1.16x faster                                                           |
Ignored benchmarks (18) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp_ssl, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, richards_super, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.14x
- 95% likely to have a speedup of 1.12x
- 99% likely to have a speedup of 1.09x
