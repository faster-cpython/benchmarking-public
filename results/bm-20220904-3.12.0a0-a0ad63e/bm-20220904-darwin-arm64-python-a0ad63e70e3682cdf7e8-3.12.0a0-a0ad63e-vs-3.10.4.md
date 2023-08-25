
# Results vs. 3.10.4

- fork: python
- ref: a0ad63e70e3682cdf7e8
- machine: darwin-arm64
- commit hash: a0ad63e
- commit date: 2022-09-04
- overall geometric mean: 1.23x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.18x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20220904-darwin-arm64-python-a0ad63e70e3682cdf7e8-3.12.0a0-a0ad63e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 202 ms                                                 | 185 ms: 1.10x faster                                                  |
| chameleon      | 5.84 ms                                                | 4.59 ms: 1.27x faster                                                 |
| docutils       | 1.78 sec                                               | 1.48 sec: 1.21x faster                                                |
| html5lib       | 44.1 ms                                                | 36.4 ms: 1.21x faster                                                 |
| tornado_http   | 91.9 ms                                                | 70.1 ms: 1.31x faster                                                 |
| Geometric mean | (ref)                                                  | 1.22x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20220904-darwin-arm64-python-a0ad63e70e3682cdf7e8-3.12.0a0-a0ad63e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 94.1 ms                                                | 64.0 ms: 1.47x faster                                                 |
| float          | 72.3 ms                                                | 51.3 ms: 1.41x faster                                                 |
| Geometric mean | (ref)                                                  | 1.28x faster                                                          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20220904-darwin-arm64-python-a0ad63e70e3682cdf7e8-3.12.0a0-a0ad63e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 96.6 ms                                                | 75.3 ms: 1.28x faster                                                 |
| regex_v8       | 17.5 ms                                                | 16.4 ms: 1.07x faster                                                 |
| regex_dna      | 160 ms                                                 | 151 ms: 1.06x faster                                                  |
| regex_effbot   | 2.45 ms                                                | 2.72 ms: 1.11x slower                                                 |
| Geometric mean | (ref)                                                  | 1.07x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20220904-darwin-arm64-python-a0ad63e70e3682cdf7e8-3.12.0a0-a0ad63e |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 284 us                                                 | 198 us: 1.43x faster                                                  |
| json_dumps           | 8.38 ms                                                | 6.10 ms: 1.37x faster                                                 |
| xml_etree_process    | 45.1 ms                                                | 34.5 ms: 1.31x faster                                                 |
| unpickle_pure_python | 203 us                                                 | 160 us: 1.27x faster                                                  |
| xml_etree_generate   | 54.3 ms                                                | 47.2 ms: 1.15x faster                                                 |
| xml_etree_iterparse  | 72.6 ms                                                | 64.5 ms: 1.13x faster                                                 |
| xml_etree_parse      | 107 ms                                                 | 95.9 ms: 1.12x faster                                                 |
| json_loads           | 16.9 us                                                | 16.2 us: 1.04x faster                                                 |
| unpickle_list        | 2.66 us                                                | 2.58 us: 1.03x faster                                                 |
| unpickle             | 9.77 us                                                | 9.64 us: 1.01x faster                                                 |
| pickle_list          | 2.83 us                                                | 2.85 us: 1.01x slower                                                 |
| pickle_dict          | 17.8 us                                                | 18.0 us: 1.01x slower                                                 |
| pickle               | 7.36 us                                                | 7.59 us: 1.03x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.13x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20220904-darwin-arm64-python-a0ad63e70e3682cdf7e8-3.12.0a0-a0ad63e |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 12.6 ms                                                | 9.07 ms: 1.39x faster                                                 |
| python_startup_no_site | 9.73 ms                                                | 7.16 ms: 1.36x faster                                                 |
| Geometric mean         | (ref)                                                  | 1.37x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20220904-darwin-arm64-python-a0ad63e70e3682cdf7e8-3.12.0a0-a0ad63e |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 10.5 ms                                                | 7.97 ms: 1.32x faster                                                 |
| django_template | 27.3 ms                                                | 20.9 ms: 1.31x faster                                                 |
| genshi_xml      | 37.6 ms                                                | 29.9 ms: 1.26x faster                                                 |
| genshi_text     | 18.4 ms                                                | 15.1 ms: 1.22x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.27x faster                                                          |

All benchmarks:
===============

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20220904-darwin-arm64-python-a0ad63e70e3682cdf7e8-3.12.0a0-a0ad63e |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| logging_silent          | 119 ns                                                 | 64.5 ns: 1.85x faster                                                 |
| deltablue               | 5.15 ms                                                | 2.84 ms: 1.82x faster                                                 |
| raytrace                | 328 ms                                                 | 211 ms: 1.55x faster                                                  |
| richards                | 51.4 ms                                                | 33.4 ms: 1.54x faster                                                 |
| crypto_pyaes            | 78.0 ms                                                | 51.1 ms: 1.53x faster                                                 |
| scimark_lu              | 110 ms                                                 | 72.7 ms: 1.51x faster                                                 |
| nbody                   | 94.1 ms                                                | 64.0 ms: 1.47x faster                                                 |
| pickle_pure_python      | 284 us                                                 | 198 us: 1.43x faster                                                  |
| async_tree_none         | 402 ms                                                 | 284 ms: 1.42x faster                                                  |
| float                   | 72.3 ms                                                | 51.3 ms: 1.41x faster                                                 |
| go                      | 165 ms                                                 | 117 ms: 1.41x faster                                                  |
| deepcopy_memo           | 34.5 us                                                | 24.8 us: 1.39x faster                                                 |
| python_startup          | 12.6 ms                                                | 9.07 ms: 1.39x faster                                                 |
| async_tree_io           | 1.02 sec                                               | 734 ms: 1.39x faster                                                  |
| pathlib                 | 28.8 ms                                                | 20.8 ms: 1.39x faster                                                 |
| json_dumps              | 8.38 ms                                                | 6.10 ms: 1.37x faster                                                 |
| python_startup_no_site  | 9.73 ms                                                | 7.16 ms: 1.36x faster                                                 |
| chaos                   | 66.8 ms                                                | 49.5 ms: 1.35x faster                                                 |
| spectral_norm           | 96.4 ms                                                | 71.7 ms: 1.34x faster                                                 |
| scimark_monte_carlo     | 72.2 ms                                                | 53.8 ms: 1.34x faster                                                 |
| thrift                  | 586 us                                                 | 441 us: 1.33x faster                                                  |
| sqlglot_parse           | 1.33 ms                                                | 1.00 ms: 1.33x faster                                                 |
| sqlglot_transpile       | 1.54 ms                                                | 1.16 ms: 1.32x faster                                                 |
| mako                    | 10.5 ms                                                | 7.97 ms: 1.32x faster                                                 |
| pyflate                 | 453 ms                                                 | 345 ms: 1.31x faster                                                  |
| tornado_http            | 91.9 ms                                                | 70.1 ms: 1.31x faster                                                 |
| pprint_pformat          | 1.24 sec                                               | 949 ms: 1.31x faster                                                  |
| xml_etree_process       | 45.1 ms                                                | 34.5 ms: 1.31x faster                                                 |
| django_template         | 27.3 ms                                                | 20.9 ms: 1.31x faster                                                 |
| hexiom                  | 6.32 ms                                                | 4.84 ms: 1.31x faster                                                 |
| pprint_safe_repr        | 609 ms                                                 | 468 ms: 1.30x faster                                                  |
| async_tree_memoization  | 493 ms                                                 | 381 ms: 1.29x faster                                                  |
| deepcopy                | 278 us                                                 | 215 us: 1.29x faster                                                  |
| deepcopy_reduce         | 2.38 us                                                | 1.85 us: 1.29x faster                                                 |
| pycparser               | 915 ms                                                 | 711 ms: 1.29x faster                                                  |
| regex_compile           | 96.6 ms                                                | 75.3 ms: 1.28x faster                                                 |
| logging_format          | 5.01 us                                                | 3.92 us: 1.28x faster                                                 |
| scimark_sor             | 127 ms                                                 | 99.0 ms: 1.28x faster                                                 |
| logging_simple          | 4.63 us                                                | 3.63 us: 1.28x faster                                                 |
| chameleon               | 5.84 ms                                                | 4.59 ms: 1.27x faster                                                 |
| unpickle_pure_python    | 203 us                                                 | 160 us: 1.27x faster                                                  |
| sqlalchemy_imperative   | 9.03 ms                                                | 7.12 ms: 1.27x faster                                                 |
| async_tree_cpu_io_mixed | 670 ms                                                 | 530 ms: 1.26x faster                                                  |
| genshi_xml              | 37.6 ms                                                | 29.9 ms: 1.26x faster                                                 |
| dulwich_log             | 37.1 ms                                                | 29.5 ms: 1.26x faster                                                 |
| scimark_sparse_mat_mult | 3.47 ms                                                | 2.80 ms: 1.24x faster                                                 |
| flaskblogging           | 2.75 ms                                                | 2.22 ms: 1.24x faster                                                 |
| bench_thread_pool       | 548 us                                                 | 449 us: 1.22x faster                                                  |
| genshi_text             | 18.4 ms                                                | 15.1 ms: 1.22x faster                                                 |
| sqlalchemy_declarative  | 74.8 ms                                                | 61.5 ms: 1.22x faster                                                 |
| html5lib                | 44.1 ms                                                | 36.4 ms: 1.21x faster                                                 |
| docutils                | 1.78 sec                                               | 1.48 sec: 1.21x faster                                                |
| sqlglot_optimize        | 38.0 ms                                                | 31.7 ms: 1.20x faster                                                 |
| fannkuch                | 317 ms                                                 | 268 ms: 1.18x faster                                                  |
| scimark_fft             | 232 ms                                                 | 197 ms: 1.18x faster                                                  |
| unpack_sequence         | 38.7 ns                                                | 33.0 ns: 1.17x faster                                                 |
| async_generators        | 233 ms                                                 | 199 ms: 1.17x faster                                                  |
| sympy_integrate         | 13.4 ms                                                | 11.5 ms: 1.17x faster                                                 |
| pylint                  | 307 ms                                                 | 264 ms: 1.16x faster                                                  |
| nqueens                 | 68.1 ms                                                | 58.7 ms: 1.16x faster                                                 |
| xml_etree_generate      | 54.3 ms                                                | 47.2 ms: 1.15x faster                                                 |
| sqlglot_normalize       | 197 ms                                                 | 172 ms: 1.15x faster                                                  |
| generators              | 32.9 ms                                                | 29.1 ms: 1.13x faster                                                 |
| xml_etree_iterparse     | 72.6 ms                                                | 64.5 ms: 1.13x faster                                                 |
| sympy_sum               | 94.3 ms                                                | 84.0 ms: 1.12x faster                                                 |
| xml_etree_parse         | 107 ms                                                 | 95.9 ms: 1.12x faster                                                 |
| sympy_expand            | 276 ms                                                 | 247 ms: 1.12x faster                                                  |
| sympy_str               | 169 ms                                                 | 152 ms: 1.12x faster                                                  |
| telco                   | 3.68 ms                                                | 3.34 ms: 1.10x faster                                                 |
| json                    | 3.10 ms                                                | 2.82 ms: 1.10x faster                                                 |
| 2to3                    | 202 ms                                                 | 185 ms: 1.10x faster                                                  |
| mdp                     | 1.67 sec                                               | 1.55 sec: 1.08x faster                                                |
| regex_v8                | 17.5 ms                                                | 16.4 ms: 1.07x faster                                                 |
| regex_dna               | 160 ms                                                 | 151 ms: 1.06x faster                                                  |
| sqlite_synth            | 1.47 us                                                | 1.40 us: 1.05x faster                                                 |
| coroutines              | 20.2 ms                                                | 19.3 ms: 1.04x faster                                                 |
| json_loads              | 16.9 us                                                | 16.2 us: 1.04x faster                                                 |
| unpickle_list           | 2.66 us                                                | 2.58 us: 1.03x faster                                                 |
| meteor_contest          | 78.6 ms                                                | 77.0 ms: 1.02x faster                                                 |
| unpickle                | 9.77 us                                                | 9.64 us: 1.01x faster                                                 |
| pickle_list             | 2.83 us                                                | 2.85 us: 1.01x slower                                                 |
| pickle_dict             | 17.8 us                                                | 18.0 us: 1.01x slower                                                 |
| pickle                  | 7.36 us                                                | 7.59 us: 1.03x slower                                                 |
| regex_effbot            | 2.45 ms                                                | 2.72 ms: 1.11x slower                                                 |
| coverage                | 40.8 ms                                                | 54.3 ms: 1.33x slower                                                 |
| Geometric mean          | (ref)                                                  | 1.23x faster                                                          |

Benchmark hidden because not significant (2): bench_mp_pool, pidigits
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, comprehensions, create_gc_cycles, dask, gc_traversal, gunicorn, mypy2, richards_super, tomli_loads, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20220904-3.12.0a0-a0ad63e/bm-20220904-darwin-arm64-python-a0ad63e70e3682cdf7e8-3.12.0a0-a0ad63e.json: mypy


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.21x
- 95% likely to have a speedup of 1.20x
- 99% likely to have a speedup of 1.18x
