
# Results vs. 3.10.4

- fork: python
- ref: b1b375e2670a58fc37cb
- machine: darwin-arm64
- commit hash: b1b375e
- commit date: 2023-02-19
- overall geometric mean: 1.21x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.18x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230219-darwin-arm64-python-b1b375e2670a58fc37cb-3.12.0a5+-b1b375e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 202 ms                                                 | 162 ms: 1.25x faster                                                   |
| chameleon      | 5.84 ms                                                | 4.44 ms: 1.32x faster                                                  |
| docutils       | 1.78 sec                                               | 1.49 sec: 1.20x faster                                                 |
| html5lib       | 44.1 ms                                                | 35.8 ms: 1.23x faster                                                  |
| tornado_http   | 91.9 ms                                                | 70.3 ms: 1.31x faster                                                  |
| Geometric mean | (ref)                                                  | 1.26x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230219-darwin-arm64-python-b1b375e2670a58fc37cb-3.12.0a5+-b1b375e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 94.1 ms                                                | 64.1 ms: 1.47x faster                                                  |
| float          | 72.3 ms                                                | 52.4 ms: 1.38x faster                                                  |
| pidigits       | 282 ms                                                 | 281 ms: 1.00x faster                                                   |
| Geometric mean | (ref)                                                  | 1.27x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230219-darwin-arm64-python-b1b375e2670a58fc37cb-3.12.0a5+-b1b375e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 96.6 ms                                                | 73.0 ms: 1.32x faster                                                  |
| regex_v8       | 17.5 ms                                                | 15.8 ms: 1.11x faster                                                  |
| regex_dna      | 160 ms                                                 | 149 ms: 1.07x faster                                                   |
| regex_effbot   | 2.45 ms                                                | 2.63 ms: 1.08x slower                                                  |
| Geometric mean | (ref)                                                  | 1.10x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230219-darwin-arm64-python-b1b375e2670a58fc37cb-3.12.0a5+-b1b375e |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_pure_python   | 284 us                                                 | 195 us: 1.46x faster                                                   |
| unpickle_pure_python | 203 us                                                 | 143 us: 1.43x faster                                                   |
| json_dumps           | 8.38 ms                                                | 6.15 ms: 1.36x faster                                                  |
| xml_etree_process    | 45.1 ms                                                | 36.0 ms: 1.25x faster                                                  |
| xml_etree_parse      | 107 ms                                                 | 97.6 ms: 1.10x faster                                                  |
| xml_etree_generate   | 54.3 ms                                                | 50.3 ms: 1.08x faster                                                  |
| json_loads           | 16.9 us                                                | 16.1 us: 1.05x faster                                                  |
| unpickle_list        | 2.66 us                                                | 2.57 us: 1.04x faster                                                  |
| xml_etree_iterparse  | 72.6 ms                                                | 70.9 ms: 1.02x faster                                                  |
| unpickle             | 9.77 us                                                | 9.65 us: 1.01x faster                                                  |
| pickle_dict          | 17.8 us                                                | 18.1 us: 1.02x slower                                                  |
| pickle               | 7.36 us                                                | 7.56 us: 1.03x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.12x faster                                                           |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230219-darwin-arm64-python-b1b375e2670a58fc37cb-3.12.0a5+-b1b375e |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 12.6 ms                                                | 12.4 ms: 1.02x faster                                                  |
| python_startup_no_site | 9.73 ms                                                | 10.4 ms: 1.07x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.03x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230219-darwin-arm64-python-b1b375e2670a58fc37cb-3.12.0a5+-b1b375e |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 10.5 ms                                                | 7.36 ms: 1.42x faster                                                  |
| genshi_xml      | 37.6 ms                                                | 28.3 ms: 1.33x faster                                                  |
| genshi_text     | 18.4 ms                                                | 14.3 ms: 1.28x faster                                                  |
| django_template | 27.3 ms                                                | 21.3 ms: 1.28x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.33x faster                                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230219-darwin-arm64-python-b1b375e2670a58fc37cb-3.12.0a5+-b1b375e |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| deltablue               | 5.15 ms                                                | 2.57 ms: 2.00x faster                                                  |
| logging_silent          | 119 ns                                                 | 65.8 ns: 1.81x faster                                                  |
| richards                | 51.4 ms                                                | 30.0 ms: 1.71x faster                                                  |
| asyncio_tcp             | 673 ms                                                 | 441 ms: 1.53x faster                                                   |
| go                      | 165 ms                                                 | 109 ms: 1.51x faster                                                   |
| scimark_lu              | 110 ms                                                 | 73.3 ms: 1.50x faster                                                  |
| async_tree_memoization  | 493 ms                                                 | 329 ms: 1.50x faster                                                   |
| raytrace                | 328 ms                                                 | 223 ms: 1.47x faster                                                   |
| nbody                   | 94.1 ms                                                | 64.1 ms: 1.47x faster                                                  |
| hexiom                  | 6.32 ms                                                | 4.31 ms: 1.47x faster                                                  |
| scimark_sor             | 127 ms                                                 | 86.5 ms: 1.46x faster                                                  |
| crypto_pyaes            | 78.0 ms                                                | 53.5 ms: 1.46x faster                                                  |
| pickle_pure_python      | 284 us                                                 | 195 us: 1.46x faster                                                   |
| chaos                   | 66.8 ms                                                | 46.6 ms: 1.43x faster                                                  |
| unpickle_pure_python    | 203 us                                                 | 143 us: 1.43x faster                                                   |
| mako                    | 10.5 ms                                                | 7.36 ms: 1.42x faster                                                  |
| async_tree_none         | 402 ms                                                 | 286 ms: 1.40x faster                                                   |
| pyflate                 | 453 ms                                                 | 328 ms: 1.38x faster                                                   |
| float                   | 72.3 ms                                                | 52.4 ms: 1.38x faster                                                  |
| scimark_monte_carlo     | 72.2 ms                                                | 52.7 ms: 1.37x faster                                                  |
| async_tree_io           | 1.02 sec                                               | 745 ms: 1.37x faster                                                   |
| pycparser               | 915 ms                                                 | 669 ms: 1.37x faster                                                   |
| json_dumps              | 8.38 ms                                                | 6.15 ms: 1.36x faster                                                  |
| deepcopy_memo           | 34.5 us                                                | 25.5 us: 1.35x faster                                                  |
| genshi_xml              | 37.6 ms                                                | 28.3 ms: 1.33x faster                                                  |
| regex_compile           | 96.6 ms                                                | 73.0 ms: 1.32x faster                                                  |
| chameleon               | 5.84 ms                                                | 4.44 ms: 1.32x faster                                                  |
| tornado_http            | 91.9 ms                                                | 70.3 ms: 1.31x faster                                                  |
| pprint_safe_repr        | 609 ms                                                 | 468 ms: 1.30x faster                                                   |
| pprint_pformat          | 1.24 sec                                               | 954 ms: 1.30x faster                                                   |
| generators              | 32.9 ms                                                | 25.5 ms: 1.29x faster                                                  |
| genshi_text             | 18.4 ms                                                | 14.3 ms: 1.28x faster                                                  |
| spectral_norm           | 96.4 ms                                                | 75.2 ms: 1.28x faster                                                  |
| logging_format          | 5.01 us                                                | 3.91 us: 1.28x faster                                                  |
| django_template         | 27.3 ms                                                | 21.3 ms: 1.28x faster                                                  |
| logging_simple          | 4.63 us                                                | 3.64 us: 1.27x faster                                                  |
| thrift                  | 586 us                                                 | 461 us: 1.27x faster                                                   |
| sqlglot_parse           | 1.33 ms                                                | 1.05 ms: 1.27x faster                                                  |
| deepcopy                | 278 us                                                 | 221 us: 1.26x faster                                                   |
| sqlglot_transpile       | 1.54 ms                                                | 1.22 ms: 1.26x faster                                                  |
| dulwich_log             | 37.1 ms                                                | 29.5 ms: 1.26x faster                                                  |
| 2to3                    | 202 ms                                                 | 162 ms: 1.25x faster                                                   |
| xml_etree_process       | 45.1 ms                                                | 36.0 ms: 1.25x faster                                                  |
| deepcopy_reduce         | 2.38 us                                                | 1.91 us: 1.25x faster                                                  |
| sqlalchemy_imperative   | 9.03 ms                                                | 7.23 ms: 1.25x faster                                                  |
| create_gc_cycles        | 876 us                                                 | 703 us: 1.25x faster                                                   |
| async_tree_cpu_io_mixed | 670 ms                                                 | 542 ms: 1.24x faster                                                   |
| fannkuch                | 317 ms                                                 | 257 ms: 1.24x faster                                                   |
| scimark_sparse_mat_mult | 3.47 ms                                                | 2.82 ms: 1.23x faster                                                  |
| html5lib                | 44.1 ms                                                | 35.8 ms: 1.23x faster                                                  |
| scimark_fft             | 232 ms                                                 | 194 ms: 1.20x faster                                                   |
| docutils                | 1.78 sec                                               | 1.49 sec: 1.20x faster                                                 |
| sqlglot_optimize        | 38.0 ms                                                | 31.9 ms: 1.19x faster                                                  |
| unpack_sequence         | 38.7 ns                                                | 32.7 ns: 1.18x faster                                                  |
| mypy2                   | 308 ms                                                 | 261 ms: 1.18x faster                                                   |
| sympy_integrate         | 13.4 ms                                                | 11.3 ms: 1.18x faster                                                  |
| bench_thread_pool       | 548 us                                                 | 466 us: 1.18x faster                                                   |
| comprehensions          | 17.7 us                                                | 15.1 us: 1.17x faster                                                  |
| sqlalchemy_declarative  | 74.8 ms                                                | 63.9 ms: 1.17x faster                                                  |
| sympy_str               | 169 ms                                                 | 147 ms: 1.15x faster                                                   |
| sympy_expand            | 276 ms                                                 | 243 ms: 1.13x faster                                                   |
| coroutines              | 20.2 ms                                                | 17.8 ms: 1.13x faster                                                  |
| sqlglot_normalize       | 197 ms                                                 | 174 ms: 1.13x faster                                                   |
| sympy_sum               | 94.3 ms                                                | 83.8 ms: 1.13x faster                                                  |
| json                    | 3.10 ms                                                | 2.77 ms: 1.12x faster                                                  |
| nqueens                 | 68.1 ms                                                | 61.1 ms: 1.11x faster                                                  |
| regex_v8                | 17.5 ms                                                | 15.8 ms: 1.11x faster                                                  |
| xml_etree_parse         | 107 ms                                                 | 97.6 ms: 1.10x faster                                                  |
| sqlite_synth            | 1.47 us                                                | 1.35 us: 1.09x faster                                                  |
| mdp                     | 1.67 sec                                               | 1.54 sec: 1.08x faster                                                 |
| xml_etree_generate      | 54.3 ms                                                | 50.3 ms: 1.08x faster                                                  |
| regex_dna               | 160 ms                                                 | 149 ms: 1.07x faster                                                   |
| pathlib                 | 28.8 ms                                                | 27.0 ms: 1.07x faster                                                  |
| telco                   | 3.68 ms                                                | 3.48 ms: 1.06x faster                                                  |
| json_loads              | 16.9 us                                                | 16.1 us: 1.05x faster                                                  |
| unpickle_list           | 2.66 us                                                | 2.57 us: 1.04x faster                                                  |
| meteor_contest          | 78.6 ms                                                | 76.3 ms: 1.03x faster                                                  |
| xml_etree_iterparse     | 72.6 ms                                                | 70.9 ms: 1.02x faster                                                  |
| python_startup          | 12.6 ms                                                | 12.4 ms: 1.02x faster                                                  |
| unpickle                | 9.77 us                                                | 9.65 us: 1.01x faster                                                  |
| pidigits                | 282 ms                                                 | 281 ms: 1.00x faster                                                   |
| gc_traversal            | 2.40 ms                                                | 2.42 ms: 1.01x slower                                                  |
| pickle_dict             | 17.8 us                                                | 18.1 us: 1.02x slower                                                  |
| pickle                  | 7.36 us                                                | 7.56 us: 1.03x slower                                                  |
| python_startup_no_site  | 9.73 ms                                                | 10.4 ms: 1.07x slower                                                  |
| regex_effbot            | 2.45 ms                                                | 2.63 ms: 1.08x slower                                                  |
| bench_mp_pool           | 41.0 ms                                                | 46.2 ms: 1.13x slower                                                  |
| async_generators        | 233 ms                                                 | 264 ms: 1.13x slower                                                   |
| dask                    | 258 ms                                                 | 321 ms: 1.25x slower                                                   |
| coverage                | 40.8 ms                                                | 60.9 ms: 1.49x slower                                                  |
| Geometric mean          | (ref)                                                  | 1.21x faster                                                           |

Benchmark hidden because not significant (1): pickle_list
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp_ssl, flaskblogging, gunicorn, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.21x
- 95% likely to have a speedup of 1.19x
- 99% likely to have a speedup of 1.18x
