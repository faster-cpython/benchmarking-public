
# Results vs. 3.10.4

- fork: python
- ref: 3b9d793efcfd2c00c14f
- machine: darwin-arm64
- commit hash: 3b9d793
- commit date: 2022-11-14
- overall geometric mean: 1.18x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.14x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221114-darwin-arm64-python-3b9d793efcfd2c00c14f-3.12.0a2-3b9d793 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 202 ms                                                 | 167 ms: 1.21x faster                                                  |
| chameleon      | 5.84 ms                                                | 4.44 ms: 1.32x faster                                                 |
| docutils       | 1.78 sec                                               | 1.48 sec: 1.21x faster                                                |
| html5lib       | 44.1 ms                                                | 35.9 ms: 1.23x faster                                                 |
| tornado_http   | 91.9 ms                                                | 71.3 ms: 1.29x faster                                                 |
| Geometric mean | (ref)                                                  | 1.25x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221114-darwin-arm64-python-3b9d793efcfd2c00c14f-3.12.0a2-3b9d793 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 94.1 ms                                                | 65.8 ms: 1.43x faster                                                 |
| float          | 72.3 ms                                                | 56.3 ms: 1.28x faster                                                 |
| pidigits       | 282 ms                                                 | 281 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                  | 1.23x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221114-darwin-arm64-python-3b9d793efcfd2c00c14f-3.12.0a2-3b9d793 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 96.6 ms                                                | 76.0 ms: 1.27x faster                                                 |
| regex_v8       | 17.5 ms                                                | 15.7 ms: 1.12x faster                                                 |
| regex_dna      | 160 ms                                                 | 149 ms: 1.07x faster                                                  |
| regex_effbot   | 2.45 ms                                                | 2.60 ms: 1.06x slower                                                 |
| Geometric mean | (ref)                                                  | 1.09x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221114-darwin-arm64-python-3b9d793efcfd2c00c14f-3.12.0a2-3b9d793 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 284 us                                                 | 205 us: 1.38x faster                                                  |
| json_dumps           | 8.38 ms                                                | 6.12 ms: 1.37x faster                                                 |
| xml_etree_process    | 45.1 ms                                                | 35.5 ms: 1.27x faster                                                 |
| unpickle_pure_python | 203 us                                                 | 162 us: 1.26x faster                                                  |
| xml_etree_parse      | 107 ms                                                 | 96.3 ms: 1.11x faster                                                 |
| xml_etree_generate   | 54.3 ms                                                | 48.7 ms: 1.11x faster                                                 |
| xml_etree_iterparse  | 72.6 ms                                                | 69.6 ms: 1.04x faster                                                 |
| json_loads           | 16.9 us                                                | 16.2 us: 1.04x faster                                                 |
| unpickle_list        | 2.66 us                                                | 2.59 us: 1.03x faster                                                 |
| pickle_list          | 2.83 us                                                | 2.85 us: 1.01x slower                                                 |
| pickle               | 7.36 us                                                | 7.44 us: 1.01x slower                                                 |
| pickle_dict          | 17.8 us                                                | 18.0 us: 1.01x slower                                                 |
| unpickle             | 9.77 us                                                | 9.94 us: 1.02x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.11x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221114-darwin-arm64-python-3b9d793efcfd2c00c14f-3.12.0a2-3b9d793 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 12.6 ms                                                | 12.3 ms: 1.02x faster                                                 |
| python_startup_no_site | 9.73 ms                                                | 10.2 ms: 1.05x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221114-darwin-arm64-python-3b9d793efcfd2c00c14f-3.12.0a2-3b9d793 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 10.5 ms                                                | 7.18 ms: 1.46x faster                                                 |
| django_template | 27.3 ms                                                | 21.4 ms: 1.27x faster                                                 |
| genshi_xml      | 37.6 ms                                                | 29.6 ms: 1.27x faster                                                 |
| genshi_text     | 18.4 ms                                                | 14.8 ms: 1.25x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.31x faster                                                          |

All benchmarks:
===============

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221114-darwin-arm64-python-3b9d793efcfd2c00c14f-3.12.0a2-3b9d793 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deltablue               | 5.15 ms                                                | 2.68 ms: 1.92x faster                                                 |
| logging_silent          | 119 ns                                                 | 67.1 ns: 1.77x faster                                                 |
| richards                | 51.4 ms                                                | 32.0 ms: 1.61x faster                                                 |
| scimark_lu              | 110 ms                                                 | 70.0 ms: 1.57x faster                                                 |
| raytrace                | 328 ms                                                 | 214 ms: 1.53x faster                                                  |
| crypto_pyaes            | 78.0 ms                                                | 51.9 ms: 1.50x faster                                                 |
| mako                    | 10.5 ms                                                | 7.18 ms: 1.46x faster                                                 |
| async_tree_memoization  | 493 ms                                                 | 338 ms: 1.46x faster                                                  |
| nbody                   | 94.1 ms                                                | 65.8 ms: 1.43x faster                                                 |
| go                      | 165 ms                                                 | 119 ms: 1.38x faster                                                  |
| pickle_pure_python      | 284 us                                                 | 205 us: 1.38x faster                                                  |
| json_dumps              | 8.38 ms                                                | 6.12 ms: 1.37x faster                                                 |
| async_tree_none         | 402 ms                                                 | 294 ms: 1.37x faster                                                  |
| async_tree_io           | 1.02 sec                                               | 755 ms: 1.35x faster                                                  |
| thrift                  | 586 us                                                 | 442 us: 1.33x faster                                                  |
| sqlglot_parse           | 1.33 ms                                                | 1.01 ms: 1.32x faster                                                 |
| scimark_monte_carlo     | 72.2 ms                                                | 54.6 ms: 1.32x faster                                                 |
| spectral_norm           | 96.4 ms                                                | 73.0 ms: 1.32x faster                                                 |
| chameleon               | 5.84 ms                                                | 4.44 ms: 1.32x faster                                                 |
| pycparser               | 915 ms                                                 | 696 ms: 1.31x faster                                                  |
| sqlglot_transpile       | 1.54 ms                                                | 1.17 ms: 1.31x faster                                                 |
| chaos                   | 66.8 ms                                                | 51.0 ms: 1.31x faster                                                 |
| pyflate                 | 453 ms                                                 | 351 ms: 1.29x faster                                                  |
| tornado_http            | 91.9 ms                                                | 71.3 ms: 1.29x faster                                                 |
| float                   | 72.3 ms                                                | 56.3 ms: 1.28x faster                                                 |
| logging_format          | 5.01 us                                                | 3.92 us: 1.28x faster                                                 |
| logging_simple          | 4.63 us                                                | 3.63 us: 1.28x faster                                                 |
| django_template         | 27.3 ms                                                | 21.4 ms: 1.27x faster                                                 |
| genshi_xml              | 37.6 ms                                                | 29.6 ms: 1.27x faster                                                 |
| regex_compile           | 96.6 ms                                                | 76.0 ms: 1.27x faster                                                 |
| xml_etree_process       | 45.1 ms                                                | 35.5 ms: 1.27x faster                                                 |
| create_gc_cycles        | 876 us                                                 | 693 us: 1.27x faster                                                  |
| unpickle_pure_python    | 203 us                                                 | 162 us: 1.26x faster                                                  |
| hexiom                  | 6.32 ms                                                | 5.04 ms: 1.25x faster                                                 |
| scimark_sparse_mat_mult | 3.47 ms                                                | 2.79 ms: 1.25x faster                                                 |
| genshi_text             | 18.4 ms                                                | 14.8 ms: 1.25x faster                                                 |
| pprint_pformat          | 1.24 sec                                               | 1.01 sec: 1.23x faster                                                |
| dulwich_log             | 37.1 ms                                                | 30.2 ms: 1.23x faster                                                 |
| html5lib                | 44.1 ms                                                | 35.9 ms: 1.23x faster                                                 |
| pprint_safe_repr        | 609 ms                                                 | 497 ms: 1.22x faster                                                  |
| 2to3                    | 202 ms                                                 | 167 ms: 1.21x faster                                                  |
| async_tree_cpu_io_mixed | 670 ms                                                 | 555 ms: 1.21x faster                                                  |
| docutils                | 1.78 sec                                               | 1.48 sec: 1.21x faster                                                |
| scimark_sor             | 127 ms                                                 | 105 ms: 1.21x faster                                                  |
| sqlglot_optimize        | 38.0 ms                                                | 31.8 ms: 1.20x faster                                                 |
| fannkuch                | 317 ms                                                 | 271 ms: 1.17x faster                                                  |
| deepcopy_memo           | 34.5 us                                                | 29.5 us: 1.17x faster                                                 |
| scimark_fft             | 232 ms                                                 | 198 ms: 1.17x faster                                                  |
| mypy2                   | 308 ms                                                 | 264 ms: 1.17x faster                                                  |
| bench_thread_pool       | 548 us                                                 | 473 us: 1.16x faster                                                  |
| deepcopy_reduce         | 2.38 us                                                | 2.07 us: 1.15x faster                                                 |
| deepcopy                | 278 us                                                 | 243 us: 1.14x faster                                                  |
| sympy_integrate         | 13.4 ms                                                | 11.7 ms: 1.14x faster                                                 |
| sqlglot_normalize       | 197 ms                                                 | 174 ms: 1.13x faster                                                  |
| dask                    | 258 ms                                                 | 229 ms: 1.13x faster                                                  |
| async_generators        | 233 ms                                                 | 208 ms: 1.12x faster                                                  |
| regex_v8                | 17.5 ms                                                | 15.7 ms: 1.12x faster                                                 |
| xml_etree_parse         | 107 ms                                                 | 96.3 ms: 1.11x faster                                                 |
| xml_etree_generate      | 54.3 ms                                                | 48.7 ms: 1.11x faster                                                 |
| sympy_expand            | 276 ms                                                 | 248 ms: 1.11x faster                                                  |
| telco                   | 3.68 ms                                                | 3.35 ms: 1.10x faster                                                 |
| json                    | 3.10 ms                                                | 2.83 ms: 1.10x faster                                                 |
| sympy_str               | 169 ms                                                 | 155 ms: 1.09x faster                                                  |
| sympy_sum               | 94.3 ms                                                | 87.7 ms: 1.08x faster                                                 |
| mdp                     | 1.67 sec                                               | 1.55 sec: 1.07x faster                                                |
| regex_dna               | 160 ms                                                 | 149 ms: 1.07x faster                                                  |
| pathlib                 | 28.8 ms                                                | 26.9 ms: 1.07x faster                                                 |
| nqueens                 | 68.1 ms                                                | 63.9 ms: 1.07x faster                                                 |
| sqlite_synth            | 1.47 us                                                | 1.40 us: 1.06x faster                                                 |
| xml_etree_iterparse     | 72.6 ms                                                | 69.6 ms: 1.04x faster                                                 |
| json_loads              | 16.9 us                                                | 16.2 us: 1.04x faster                                                 |
| asyncio_tcp             | 673 ms                                                 | 650 ms: 1.04x faster                                                  |
| unpickle_list           | 2.66 us                                                | 2.59 us: 1.03x faster                                                 |
| meteor_contest          | 78.6 ms                                                | 76.7 ms: 1.03x faster                                                 |
| python_startup          | 12.6 ms                                                | 12.3 ms: 1.02x faster                                                 |
| pidigits                | 282 ms                                                 | 281 ms: 1.00x faster                                                  |
| pickle_list             | 2.83 us                                                | 2.85 us: 1.01x slower                                                 |
| gc_traversal            | 2.40 ms                                                | 2.42 ms: 1.01x slower                                                 |
| pickle                  | 7.36 us                                                | 7.44 us: 1.01x slower                                                 |
| pickle_dict             | 17.8 us                                                | 18.0 us: 1.01x slower                                                 |
| unpickle                | 9.77 us                                                | 9.94 us: 1.02x slower                                                 |
| coroutines              | 20.2 ms                                                | 20.6 ms: 1.02x slower                                                 |
| comprehensions          | 17.7 us                                                | 18.0 us: 1.02x slower                                                 |
| python_startup_no_site  | 9.73 ms                                                | 10.2 ms: 1.05x slower                                                 |
| regex_effbot            | 2.45 ms                                                | 2.60 ms: 1.06x slower                                                 |
| bench_mp_pool           | 41.0 ms                                                | 44.5 ms: 1.08x slower                                                 |
| generators              | 32.9 ms                                                | 35.8 ms: 1.09x slower                                                 |
| coverage                | 40.8 ms                                                | 60.5 ms: 1.48x slower                                                 |
| unpack_sequence         | 38.7 ns                                                | 62.8 ns: 1.62x slower                                                 |
| Geometric mean          | (ref)                                                  | 1.18x faster                                                          |
Ignored benchmarks (10) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp_ssl, flaskblogging, gunicorn, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.17x
- 95% likely to have a speedup of 1.16x
- 99% likely to have a speedup of 1.14x
