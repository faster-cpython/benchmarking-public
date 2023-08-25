
# Results vs. 3.10.4

- fork: python
- ref: 728e42fcf51cbb2108ca
- machine: darwin-arm64
- commit hash: 728e42f
- commit date: 2022-11-06
- overall geometric mean: 1.19x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.15x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221106-darwin-arm64-python-728e42fcf51cbb2108ca-3.12.0a1+-728e42f |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 202 ms                                                 | 187 ms: 1.08x faster                                                   |
| chameleon      | 5.84 ms                                                | 5.13 ms: 1.14x faster                                                  |
| docutils       | 1.78 sec                                               | 1.50 sec: 1.19x faster                                                 |
| html5lib       | 44.1 ms                                                | 37.5 ms: 1.18x faster                                                  |
| tornado_http   | 91.9 ms                                                | 70.1 ms: 1.31x faster                                                  |
| Geometric mean | (ref)                                                  | 1.18x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221106-darwin-arm64-python-728e42fcf51cbb2108ca-3.12.0a1+-728e42f |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 94.1 ms                                                | 65.9 ms: 1.43x faster                                                  |
| float          | 72.3 ms                                                | 57.3 ms: 1.26x faster                                                  |
| pidigits       | 282 ms                                                 | 282 ms: 1.00x slower                                                   |
| Geometric mean | (ref)                                                  | 1.22x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221106-darwin-arm64-python-728e42fcf51cbb2108ca-3.12.0a1+-728e42f |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 96.6 ms                                                | 77.7 ms: 1.24x faster                                                  |
| regex_v8       | 17.5 ms                                                | 16.1 ms: 1.09x faster                                                  |
| regex_dna      | 160 ms                                                 | 149 ms: 1.07x faster                                                   |
| regex_effbot   | 2.45 ms                                                | 2.63 ms: 1.08x slower                                                  |
| Geometric mean | (ref)                                                  | 1.08x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221106-darwin-arm64-python-728e42fcf51cbb2108ca-3.12.0a1+-728e42f |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| json_dumps           | 8.38 ms                                                | 6.15 ms: 1.36x faster                                                  |
| pickle_pure_python   | 284 us                                                 | 222 us: 1.28x faster                                                   |
| xml_etree_process    | 45.1 ms                                                | 36.8 ms: 1.22x faster                                                  |
| unpickle_pure_python | 203 us                                                 | 167 us: 1.22x faster                                                   |
| xml_etree_parse      | 107 ms                                                 | 93.3 ms: 1.15x faster                                                  |
| xml_etree_iterparse  | 72.6 ms                                                | 65.0 ms: 1.12x faster                                                  |
| xml_etree_generate   | 54.3 ms                                                | 50.5 ms: 1.07x faster                                                  |
| json_loads           | 16.9 us                                                | 16.4 us: 1.03x faster                                                  |
| unpickle_list        | 2.66 us                                                | 2.60 us: 1.03x faster                                                  |
| unpickle             | 9.77 us                                                | 9.86 us: 1.01x slower                                                  |
| pickle_dict          | 17.8 us                                                | 18.0 us: 1.01x slower                                                  |
| pickle_list          | 2.83 us                                                | 2.88 us: 1.02x slower                                                  |
| pickle               | 7.36 us                                                | 7.55 us: 1.03x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.10x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221106-darwin-arm64-python-728e42fcf51cbb2108ca-3.12.0a1+-728e42f |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 12.6 ms                                                | 9.32 ms: 1.35x faster                                                  |
| python_startup_no_site | 9.73 ms                                                | 7.38 ms: 1.32x faster                                                  |
| Geometric mean         | (ref)                                                  | 1.34x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221106-darwin-arm64-python-728e42fcf51cbb2108ca-3.12.0a1+-728e42f |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| django_template | 27.3 ms                                                | 22.2 ms: 1.23x faster                                                  |
| mako            | 10.5 ms                                                | 8.59 ms: 1.22x faster                                                  |
| genshi_xml      | 37.6 ms                                                | 32.4 ms: 1.16x faster                                                  |
| genshi_text     | 18.4 ms                                                | 16.2 ms: 1.14x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.19x faster                                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221106-darwin-arm64-python-728e42fcf51cbb2108ca-3.12.0a1+-728e42f |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| logging_silent          | 119 ns                                                 | 65.6 ns: 1.82x faster                                                  |
| deltablue               | 5.15 ms                                                | 2.85 ms: 1.81x faster                                                  |
| richards                | 51.4 ms                                                | 32.0 ms: 1.60x faster                                                  |
| scimark_lu              | 110 ms                                                 | 71.2 ms: 1.54x faster                                                  |
| raytrace                | 328 ms                                                 | 215 ms: 1.53x faster                                                   |
| crypto_pyaes            | 78.0 ms                                                | 51.7 ms: 1.51x faster                                                  |
| async_tree_memoization  | 493 ms                                                 | 335 ms: 1.47x faster                                                   |
| nbody                   | 94.1 ms                                                | 65.9 ms: 1.43x faster                                                  |
| pathlib                 | 28.8 ms                                                | 20.8 ms: 1.39x faster                                                  |
| async_tree_io           | 1.02 sec                                               | 736 ms: 1.39x faster                                                   |
| async_tree_none         | 402 ms                                                 | 294 ms: 1.37x faster                                                   |
| json_dumps              | 8.38 ms                                                | 6.15 ms: 1.36x faster                                                  |
| go                      | 165 ms                                                 | 121 ms: 1.36x faster                                                   |
| python_startup          | 12.6 ms                                                | 9.32 ms: 1.35x faster                                                  |
| spectral_norm           | 96.4 ms                                                | 71.9 ms: 1.34x faster                                                  |
| thrift                  | 586 us                                                 | 443 us: 1.32x faster                                                   |
| python_startup_no_site  | 9.73 ms                                                | 7.38 ms: 1.32x faster                                                  |
| scimark_monte_carlo     | 72.2 ms                                                | 54.9 ms: 1.32x faster                                                  |
| sqlglot_parse           | 1.33 ms                                                | 1.01 ms: 1.31x faster                                                  |
| tornado_http            | 91.9 ms                                                | 70.1 ms: 1.31x faster                                                  |
| sqlglot_transpile       | 1.54 ms                                                | 1.19 ms: 1.30x faster                                                  |
| chaos                   | 66.8 ms                                                | 51.6 ms: 1.29x faster                                                  |
| pycparser               | 915 ms                                                 | 711 ms: 1.29x faster                                                   |
| hexiom                  | 6.32 ms                                                | 4.91 ms: 1.29x faster                                                  |
| pyflate                 | 453 ms                                                 | 355 ms: 1.28x faster                                                   |
| pickle_pure_python      | 284 us                                                 | 222 us: 1.28x faster                                                   |
| float                   | 72.3 ms                                                | 57.3 ms: 1.26x faster                                                  |
| scimark_sparse_mat_mult | 3.47 ms                                                | 2.76 ms: 1.26x faster                                                  |
| dulwich_log             | 37.1 ms                                                | 29.7 ms: 1.25x faster                                                  |
| regex_compile           | 96.6 ms                                                | 77.7 ms: 1.24x faster                                                  |
| django_template         | 27.3 ms                                                | 22.2 ms: 1.23x faster                                                  |
| scimark_sor             | 127 ms                                                 | 103 ms: 1.23x faster                                                   |
| logging_simple          | 4.63 us                                                | 3.77 us: 1.23x faster                                                  |
| async_tree_cpu_io_mixed | 670 ms                                                 | 547 ms: 1.23x faster                                                   |
| logging_format          | 5.01 us                                                | 4.09 us: 1.22x faster                                                  |
| xml_etree_process       | 45.1 ms                                                | 36.8 ms: 1.22x faster                                                  |
| unpickle_pure_python    | 203 us                                                 | 167 us: 1.22x faster                                                   |
| mako                    | 10.5 ms                                                | 8.59 ms: 1.22x faster                                                  |
| pylint                  | 307 ms                                                 | 257 ms: 1.20x faster                                                   |
| docutils                | 1.78 sec                                               | 1.50 sec: 1.19x faster                                                 |
| sqlglot_optimize        | 38.0 ms                                                | 32.0 ms: 1.19x faster                                                  |
| bench_thread_pool       | 548 us                                                 | 463 us: 1.19x faster                                                   |
| pprint_safe_repr        | 609 ms                                                 | 514 ms: 1.18x faster                                                   |
| pprint_pformat          | 1.24 sec                                               | 1.05 sec: 1.18x faster                                                 |
| html5lib                | 44.1 ms                                                | 37.5 ms: 1.18x faster                                                  |
| generators              | 32.9 ms                                                | 28.1 ms: 1.17x faster                                                  |
| fannkuch                | 317 ms                                                 | 270 ms: 1.17x faster                                                   |
| genshi_xml              | 37.6 ms                                                | 32.4 ms: 1.16x faster                                                  |
| scimark_fft             | 232 ms                                                 | 200 ms: 1.16x faster                                                   |
| async_generators        | 233 ms                                                 | 202 ms: 1.16x faster                                                   |
| xml_etree_parse         | 107 ms                                                 | 93.3 ms: 1.15x faster                                                  |
| nqueens                 | 68.1 ms                                                | 59.3 ms: 1.15x faster                                                  |
| chameleon               | 5.84 ms                                                | 5.13 ms: 1.14x faster                                                  |
| genshi_text             | 18.4 ms                                                | 16.2 ms: 1.14x faster                                                  |
| sqlglot_normalize       | 197 ms                                                 | 175 ms: 1.13x faster                                                   |
| xml_etree_iterparse     | 72.6 ms                                                | 65.0 ms: 1.12x faster                                                  |
| sympy_integrate         | 13.4 ms                                                | 12.1 ms: 1.10x faster                                                  |
| regex_v8                | 17.5 ms                                                | 16.1 ms: 1.09x faster                                                  |
| sympy_expand            | 276 ms                                                 | 255 ms: 1.08x faster                                                   |
| json                    | 3.10 ms                                                | 2.86 ms: 1.08x faster                                                  |
| 2to3                    | 202 ms                                                 | 187 ms: 1.08x faster                                                   |
| deepcopy_memo           | 34.5 us                                                | 32.1 us: 1.08x faster                                                  |
| mdp                     | 1.67 sec                                               | 1.55 sec: 1.07x faster                                                 |
| xml_etree_generate      | 54.3 ms                                                | 50.5 ms: 1.07x faster                                                  |
| regex_dna               | 160 ms                                                 | 149 ms: 1.07x faster                                                   |
| sympy_sum               | 94.3 ms                                                | 88.0 ms: 1.07x faster                                                  |
| telco                   | 3.68 ms                                                | 3.44 ms: 1.07x faster                                                  |
| sympy_str               | 169 ms                                                 | 159 ms: 1.07x faster                                                   |
| coroutines              | 20.2 ms                                                | 19.1 ms: 1.06x faster                                                  |
| deepcopy                | 278 us                                                 | 263 us: 1.06x faster                                                   |
| deepcopy_reduce         | 2.38 us                                                | 2.28 us: 1.04x faster                                                  |
| json_loads              | 16.9 us                                                | 16.4 us: 1.03x faster                                                  |
| unpickle_list           | 2.66 us                                                | 2.60 us: 1.03x faster                                                  |
| sqlite_synth            | 1.47 us                                                | 1.45 us: 1.01x faster                                                  |
| pidigits                | 282 ms                                                 | 282 ms: 1.00x slower                                                   |
| unpickle                | 9.77 us                                                | 9.86 us: 1.01x slower                                                  |
| pickle_dict             | 17.8 us                                                | 18.0 us: 1.01x slower                                                  |
| pickle_list             | 2.83 us                                                | 2.88 us: 1.02x slower                                                  |
| meteor_contest          | 78.6 ms                                                | 80.5 ms: 1.02x slower                                                  |
| pickle                  | 7.36 us                                                | 7.55 us: 1.03x slower                                                  |
| bench_mp_pool           | 41.0 ms                                                | 42.8 ms: 1.05x slower                                                  |
| regex_effbot            | 2.45 ms                                                | 2.63 ms: 1.08x slower                                                  |
| coverage                | 40.8 ms                                                | 53.1 ms: 1.30x slower                                                  |
| unpack_sequence         | 38.7 ns                                                | 52.1 ns: 1.35x slower                                                  |
| Geometric mean          | (ref)                                                  | 1.19x faster                                                           |
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, comprehensions, create_gc_cycles, dask, flaskblogging, gc_traversal, gunicorn, mypy2, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20221106-3.12.0a1+-728e42f/bm-20221106-darwin-arm64-python-728e42fcf51cbb2108ca-3.12.0a1+-728e42f.json: mypy


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.17x
- 95% likely to have a speedup of 1.17x
- 99% likely to have a speedup of 1.15x
